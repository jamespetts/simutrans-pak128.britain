---
status: draft
verified: New master @ 30444805f
---
# Model selection for 3D and Blender work

**Covers**: which language models are suitable for AI-authored Blender geometry, and the
published measured evidence behind that choice. Read before choosing a model for an asset task,
and before claiming that a model change will or will not fix a recorded failure. Parent:
[graphics-pipelines](../graphics-pipelines.md).

Nothing here was measured on this machine. All figures are external benchmark results, tagged
`[LITERATURE:<url>]`, and none is evidence about this pakset. The pakset's own evidence is the
failure record in [blend-creation](blend-creation.md); the environment is
[blender-mcp](blender-mcp.md).

## The benchmarks worth citing

- **3DCodeEdit**, arXiv 2610.38231, 28 Oct 2026 — 2,592 instruction-guided edits over 108
  Blender programs that build entire objects; 17 models; scored from renders against
  human-reviewed checklists with no reference output. The closest published analogue to pakset
  geometry work. `[LITERATURE:https://arxiv.org/abs/2610.38231]`
- **3DCodeBench**, arXiv 2606.01057, Jun 2026 — 212 procedural object categories, 12 frontier
  models, Blender 5.0, single-shot, multi-turn, and agentic settings.
  `[LITERATURE:https://arxiv.org/abs/2606.01057]`
- **3DHarnessBench**, arXiv 2609.06535, Sep 2026 — agentic 3D-to-code reconstruction under four
  harness settings that progressively open up Blender MCP tool access, from one fixed view to
  full 3D interaction with geometric queries.
  `[LITERATURE:https://arxiv.org/abs/2609.06535]`

BlenderGym (Gu et al., CVPR 2025) is the older benchmark cited in earlier versions of
[blend-creation](blend-creation.md). Its qualitative finding still holds, but its numbers
describe 2025 models and should not be used to characterise current ones.

## Single-shot performance, by edit scope

3DCodeEdit all-pass rate (%), single shot. G1 parameter, G2 one part rebuilt, G3 two parts,
G4 structural, S style, C composition:
`[LITERATURE:https://arxiv.org/abs/2610.38231]`

| Model | G1 | G2 | G3 | G4 | S | All |
| --- | --- | --- | --- | --- | --- | --- |
| Claude Opus 5.5 | 96.5 | 76.9 | 64.4 | 58.6 | 52.5 | 69.9 |
| GPT-6.1 Sol | 95.6 | 71.3 | 65.3 | 59.3 | 57.6 | 69.1 |
| Gemini 4 Argon | 94.7 | 67.4 | 54.2 | 41.0 | 41.0 | 58.5 |
| Gemini 3.8 Flash | 94.7 | 68.8 | 62.7 | 53.7 | 34.5 | 58.4 |
| Claude Sonnet 5.5 | 91.4 | 66.4 | 51.2 | 41.9 | 25.9 | 53.7 |
| Kimi K3 (open weights) | 88.2 | 57.9 | 47.5 | 38.9 | 27.3 | 50.3 |
| Claude Haiku 5.5 | 90.3 | 54.4 | 42.8 | 31.5 | 16.0 | 44.6 |
| GPT-6 Luna | 87.0 | 51.4 | 36.6 | 29.4 | 18.8 | 41.7 |
| Qwen3.8-27B (open weights) | 84.3 | 44.2 | 28.5 | 17.1 | 3.5 | 29.9 |
| gpt-oss-120b (open weights) | 71.5 | 18.1 | 4.4 | 1.6 | 0.0 | 15.9 |

Two readings matter for pakset work. First, the scope gradient is steep: parameter edits are
mostly solved, structural edits are not. The B12/3 rebuild was a structural edit, and the best
model then available completes fewer than 60% of those. Second, mid-sized open-weight models
trail the best contemporary model by 20 to 27 points and the gap has widened as frontier models
improved (`[LITERATURE:https://arxiv.org/abs/2610.38231]`).

## Where failures come from

3DCodeEdit classifies every failure by the stage at which the edit first diverges. Below 20%
all-pass, 82% of failures are instruction comprehension, program comprehension, or code that does
not run. Above 55%, geometric foresight becomes the largest single stage at about 40%: the code
runs and builds the wrong shape. The dominant mechanisms are unforeseen interaction between
parts (9.2% of all failures), generator parameters reshaping the object unintentionally (7.3%),
and parts left floating or detached (5.3%).
`[LITERATURE:https://arxiv.org/abs/2610.38231]`

These correspond to the pakset's recorded failure modes 1 and 2 (internal incoherence,
non-propagation). 3DCodeBench reports the same pattern: "physical plausibility supersedes
executability", with disconnected parts and misaligned structures common even where the code
runs. `[LITERATURE:https://arxiv.org/abs/2606.01057]`

## Reviewer feedback is the largest single lever

3DCodeEdit, multi-turn, up to eight rounds, analysis subset:
`[LITERATURE:https://arxiv.org/abs/2610.38231]`

| Editor | single shot | own renders | reviewer pass/fail | reviewer full |
| --- | --- | --- | --- | --- |
| GPT-6.1 Sol | 64.7 | 76.0 | 75.6 | 85.6 |
| Claude Opus 5.5 | 67.6 | 74.0 | 81.7 | 83.0 |
| Claude Sonnet 5.5 | 50.6 | 55.4 | 67.3 | 71.2 |
| GPT-6 Luna | 36.9 | 49.7 | 59.0 | 65.7 |
| Qwen3.8-27B | 26.0 | 33.0 | 43.6 | 50.3 |

A separate reviewer that describes how the renders differ from each requirement beats maximum
reasoning effort (GPT-6.1 Sol reaches 74.7 at its best effort single-shot) and beats an agent
harness that renders its own output. Editors rarely revise after inspecting their own renders,
averaging under 0.6 rounds against 2.7 or more with a reviewer. The reviewer needs to judge
well, not edit well: GPT-6 Luna, which edits at 41.7, lifts Qwen3.8-27B from 37.2 to 50.3,
above Kimi K3's single-shot 46.8. `[LITERATURE:https://arxiv.org/abs/2610.38231]`

## Harness access, and what to measure instead of showing

3DHarnessBench varies target access on a fixed reconstruction objective: one fixed view, four
fixed views, agent-selected views, and full 3D interaction with geometric queries. Blender MCP
tools are available only in the last two. Every model improves with richer access, unevenly.
Two ablations bear directly on the pakset doctrine of querying the scene graph rather than
reading renders: supplying camera pose improves reconstruction substantially, while adding a
background grid barely does; and supplying part-level measurements improves topology most
(Betti L1 error 0.905 to 0.419 for Opus 5).
`[LITERATURE:https://arxiv.org/abs/2609.06535]`

Measured cost and latency per reconstruction under full 3D interaction are reported, for example
Opus 5 at $7.92 and 1,962 s and GPT-6 Astra at $3.36 and 712 s. Call efficiency, not list price,
dominates per-asset cost. `[LITERATURE:https://arxiv.org/abs/2609.06535]`

## Working position

- Cheapest credible configuration: a mid-tier editor with a separate reviewer that describes
  render differences against a checklist. The reviewer is the component worth paying for.
- Open weights: Kimi K3 is the only open-weight model within reach of the frontier on this task;
  the 27–32B open-weight models are not, for structural edits.
- Do not expect a model change to fix a structural-edit failure. Expect feedback on the result
  to narrow it.

All of this is external evidence about single procedural objects. It has not been reproduced
here, and the pakset's own failure record remains the primary evidence for the pakset.

## Open questions

- Is a local measurement worth running at all, given the recorded failure modes are already
  documented and the external benchmarks reproduce them independently?
- Which reviewer model, if any, is trusted enough for the human gate? The pakset doctrine
  currently forbids AI description of images outright ([blend-creation](blend-creation.md)).
- Does the 2.79 render step change any of the above? The benchmarks use Blender 5.x and no
  software-renderer constraint.
