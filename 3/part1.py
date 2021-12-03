import copy

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
for i in range(len(bits)-1):
    if bits[i][0] > bits[i][1]: gamma += "0"
    else:
        gamma += "1"

print(gamma)

epsilon = ""
for i in range(len(bits)-1):
    if bits[i][0] < bits[i][1]: epsilon += "0"
    else:
        epsilon += "1"

print(epsilon)


oxyData = copy.deepcopy(data)
coData = copy.deepcopy(data)

for i in range(len(gamma)-1):
    indices = []
    for d in range(len(oxyData)-1):
        if oxyData[d][i] == gamma[i]:
            print("match")
        else:
            indices.append(d)
    for index in sorted(indices, reverse=True):
        del oxyData[index]

for i in range(len(epsilon)-1):
    indices = []
    for d in range(len(coData)-1):
        if coData[d][i] == epsilon[i]:
            print("match")
        else:
            indices.append(d)
    for index in sorted(indices, reverse=True):
        del coData[index]
    print(coData)

oxyRating = int(oxyData[0],2)
coRating = int(coData[0],2)
print(oxyRating*coRating)
