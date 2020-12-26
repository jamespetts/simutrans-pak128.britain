from sys import argv
import os
objs = []
objtypes = ["building"]
popclasses = ["class_proportion[0]", "class_proportion[1]","class_proportion[2]","class_proportion[3]","class_proportion[4]"]
jobclasses = ["class_proportion_jobs[0]", "class_proportion_jobs[1]","class_proportion_jobs[2]","class_proportion_jobs[3]","class_proportion_jobs[4]"]
num_data = popclasses+jobclasses+["population_and_visitor_demand_capacity","employment_capacity","level"]
str_data = ["name","type"]

currentObj = {}

def read_file(filename):
    with open(filename,"r",encoding="latin1") as data:
        for line in data:
            if line.count("=") != 1:
                continue
            k, v = line.strip().lower().split(sep="=")
            if k == "obj":
                currentObj = {}
                if v in objtypes:
                    objs.append(currentObj)
            if k in str_data:
                currentObj[k] = v
            elif k in num_data:
                currentObj[k] = int(v)


def has(obj, key):
    return obj.get(key) is not None

def haseq(obj, key, val):
    return has(obj, key) and obj[key] == val

def hasbetween(obj, key, minval, maxval):
    return has(obj, key) and minval <= obj[key] <= maxval

def hasover(obj, key, minval):
    return has(obj, key) and minval < obj[key]

def hasanyof(obj, key, vals):
    return has(obj, key) and obj[key] in vals

def hasnoneof(obj, key, vals):
    return has(obj, key) and obj[key] not in vals

def available(obj, date):
    return obj.get("intro_year") and obj["intro_year"] <= date and (not obj.get("retire_year") or obj["retire_year"] >= date)

def bykey(obj, key):
    return obj[key] if has(obj, key) else -1

def calc_level(obj):
    pop = hasover(obj,"population_and_visitor_demand_capacity", 0)
    job = hasover(obj,"employment_capacity", 0)

    class_weight = [25,43,57,64,85] # based on passenger revenues
    class_weight_base = 50

    poptotal = 0
    if pop:
        c = obj["population_and_visitor_demand_capacity"]
        for i in range(len(popclasses)):
            poptotal += obj[popclasses[i]]*c*((class_weight_base/2)+class_weight[i])
        poptotal /= 1000*class_weight_base
        if not haseq(obj,"type","res"):
            poptotal /= 2 # weight visitors half of residents

    jobtotal = 0
    if job:
        c = obj["employment_capacity"]
        for i in range(len(jobclasses)):
            jobtotal += obj[jobclasses[i]]*c*((class_weight_base/2)+class_weight[i])
        jobtotal /= 1000*class_weight_base

    return int(poptotal+jobtotal+1)

def edit_file(filename):
    newname=filename+"_new"
    with open(filename,"r",encoding="latin1") as data:
        with open(newname,"w",encoding="latin1") as new:
            name = ""
            match = {}
            for line in data:
                if line.count("=") != 1:
                    new.write(line)
                    continue
                k, v = line.strip().lower().split(sep="=")
                if k == "name":
                    new.write(line)
                    match = {}
                    name = v
                    matches = list(filter(lambda o: haseq(o,"name",name),objs))
                    if len(matches) == 0:
                        name = ""
                        continue
                    elif len(matches) == 1:
                        match = matches[0]
                    else:
                        assert(false)
                elif k == "level" and has(match,"level"):
                    new.write(f'level={calc_level(match)}\n')
                    if calc_level(match) != match["level"]:
                        new.write(f'# Recalibrated from {match["level"]}\n')
                else:
                    new.write(line)
    os.remove(filename)
    os.rename(newname, filename)

for filename in list([f for f in os.listdir() if f.endswith(".dat")]):
    read_file(filename)
    edit_file(filename)

