# test-pakset.ps1
# Deploy the compiled pakset to the Simutrans-Extended runtime directory and run a
# headless load test against the ex-15 engine. Prints PASS or FAIL.
#
# Prerequisite: build first ( `make` inside New/ ), which produces New/pak128.Britain-Ex/.
# Usage:  powershell -ExecutionPolicy Bypass -File test-pakset.ps1
#
# The engine executable and its runtime directory are resolved relative to this file
# (New/) so the script is portable across checkouts. Update $Exe to the freshest ex-15
# build that supports -generate_map (currently Simutrans-Extended-debug-optimised.exe).

$ErrorActionPreference = 'Continue'
$NewDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$PakDir = Join-Path $NewDir 'pak128.Britain-Ex'
$EngineDir = (Resolve-Path (Join-Path $NewDir '..\..\simutrans-extended-sources\simutrans')).Path
$Exe = 'Simutrans-Extended-debug-optimised.exe'

if (-not (Test-Path (Join-Path $PakDir 'ground.Outside.pak'))) {
    Write-Output 'FAIL: compiled pakset not found - run make first.'
    exit 1
}

# Deploy the compiled pakset over the engine runtime copy.
robocopy $PakDir (Join-Path $EngineDir 'pak128.Britain-Ex') /MIR /NFL /NDL /NJH /NJS /NP | Out-Null

$outFile = Join-Path $env:TEMP 'paktest-out.txt'
$errFile = Join-Path $env:TEMP 'paktest-err.txt'
Remove-Item $outFile, $errFile -ErrorAction SilentlyContinue

$exePath = Join-Path $EngineDir $Exe
$args = @('-objects', 'pak128.Britain-Ex', '-generate_map', '-map_size', '64,64', '-log', '-nomidi', '-nosound')
$proc = Start-Process -FilePath $exePath -ArgumentList $args -WorkingDirectory $EngineDir `
    -RedirectStandardOutput $outFile -RedirectStandardError $errFile -Wait -PassThru -WindowStyle Hidden
$code = $proc.ExitCode

$outText = (Get-Content $outFile -Raw -ErrorAction SilentlyContinue) + "`n" + (Get-Content $errFile -Raw -ErrorAction SilentlyContinue)

if ($outText -match 'MAP-GEN: PASS' -and $code -eq 0) {
    Write-Output 'PASS: pakset loaded and a world was generated.'
    Write-Output (($outText -split "`r?`n" | Select-String 'MAP-GEN' | Select-Object -First 1))
    exit 0
}
else {
    Write-Output "FAIL: engine exit code $code"
    Write-Output ($outText -split "`r?`n" | Select-String -Pattern 'FATAL|ERROR|not found' | Select-Object -First 20)
    exit 1
}
