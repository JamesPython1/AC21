import copy

data = open("input.txt", "r").read().splitlines()


def countFreq(data):
    bits = [[0, 0] for i in range(len(data[0]))]

    for line in data:
        for i in range(len(line)):
            if int(line[i]) == 1: bits[i][1] += 1
            if int(line[i]) == 0: bits[i][0] += 1

    return bits

oxyData = copy.deepcopy(data)
coData = copy.deepcopy(data)

bits = countFreq(oxyData)
count = 0
while True:
    bt = countFreq(oxyData)[count]
    toRemove = []
    for it, dt in enumerate(oxyData):
        if bt[0] > bt[1]: expected = "0"
        if bt[1] > bt[0]: expected = "1"
        if bt[0] == bt[1]: expected = "1"
        print(bt, count, expected)
        if dt[count] != expected: toRemove.append(it)

    for indexToRemove in sorted(toRemove, reverse=True):
        del oxyData[indexToRemove]

    if len(oxyData) == 1:
        print("done")
        break

    print(bits)
    print(oxyData)
    count+=1

oxygenCount = oxyData[0]

# co2

bits = countFreq(coData)
count = 0
while True:
    bt = countFreq(coData)[count]
    toRemove = []
    for it, dt in enumerate(coData):
        if bt[0] < bt[1]: expected = "0"
        if bt[1] < bt[0]: expected = "1"
        if bt[0] == bt[1]: expected = "0"
        print(bt, count, expected)
        if dt[count] != expected: toRemove.append(it)

    for indexToRemove in sorted(toRemove, reverse=True):
        del coData[indexToRemove]

    if len(coData) == 1:
        print("done")
        break

    print(bits)
    print(coData)
    count+=1

coCount = coData[0]

print(oxygenCount, coCount)
print(int(oxygenCount,2) * int(coCount,2))