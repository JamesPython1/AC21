import sys, copy
sys.setrecursionlimit(1500)

data = open("input.txt", "r").read().splitlines()
bits = [[0, 0] for i in range(len(data[0]))]
print(bits)

for line in data:
    for i in range(len(line)):
        if int(line[i]) == 1: bits[i][1] += 1
        if int(line[i]) == 0: bits[i][0] += 1

# gamma (most common) and epsilon (least common)
gamma = ""

print(bits)
for i in range(len(bits)):
    if bits[i][0] == bits[i][1]: gamma+="1"
    elif bits[i][0] > bits[i][1]: gamma += "0"
    else:
        gamma += "1"

print(gamma)

epsilon = ""
for i in range(len(bits)):
    if bits[i][0] == bits[i][1]: gamma += "0"
    elif bits[i][0] > bits[i][1]: epsilon += "1"
    else:
        epsilon += "0"

print(epsilon)

# part 2 oxygen
oxyData = copy.deepcopy(data)
for i, g in enumerate(gamma):
    indicesToRemove = []
    for it, data in enumerate(oxyData):
        if data != g: indicesToRemove.append(it)
    # remove offender
    print(indicesToRemove)
    for iter, index in enumerate(indicesToRemove):
        del oxyData[index-iter]

oxygen = oxyData[0]

# part 2 co2
cData = copy.deepcopy(data)
for it, dt in enumerate(data):
    print(dt)

for i, e in enumerate(epsilon):
    indicesToRemove = []
    for it, dt in enumerate(cData):
        print(dt)
        if dt[i] != e: indicesToRemove.append(it)
    # remove offender
    for iter, index in enumerate(indicesToRemove):
        del cData[index - iter]
    print(cData)

co = cData[0]
print(oxygen)
print(co)

oxygenDenary = int(oxygen, 2)
coDenary = int(co, 2)
lsRating = oxygenDenary * coDenary
print(epsilon, gamma)
print(epsilon in data)
print(gamma in data)
print(oxyData)
print(cData)
print(lsRating)



