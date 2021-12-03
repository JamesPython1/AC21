import copy
data = open("input.txt", "r").read().splitlines()

# get frequency of 1s and 0s func
def countFreq(data):
    bits = [[0, 0] for i in range(len(data[0]))]
    for line in data:
        for i in range(len(line)):
            if int(line[i]) == 1: bits[i][1] += 1
            if int(line[i]) == 0: bits[i][0] += 1
    return bits

# copy data to avoid overwrite
oxyData = copy.deepcopy(data)
coData = copy.deepcopy(data)

# calculate oxygen and c02
count = 0
while True:
    frequency = countFreq(oxyData)[count]
    oxyToRemove = []
    # search for oxygen and ones to remove
    for it, dt in enumerate(oxyData):
        if frequency[0] > frequency[1]: oxyExpected = "0"
        if frequency[1] >= frequency[0]: oxyExpected = "1"
        if dt[count] != oxyExpected: oxyToRemove.append(it)
    for indexToRemove in sorted(oxyToRemove, reverse=True): del oxyData[indexToRemove]
    if len(oxyData) == 1: break
    count+=1

count = 0 # reset count

while True:
    frequency = countFreq(coData)[count]
    coToRemove = []
    # search for co2 and ones to remove
    for it, dt in enumerate(coData):
        if frequency[0] <= frequency[1]: coExpected = "0"
        if frequency[1] < frequency[0]: coExpected = "1"
        if dt[count] != coExpected: coToRemove.append(it)
    for indexToRemove in sorted(coToRemove, reverse=True): del coData[indexToRemove]
    if len(coData) == 1: break
    count+=1

# calculate rating and output
oxygenCount = int(oxyData[0],2)
coCount = int(coData[0],2)
airSupplyRating = oxygenCount * coCount
print(airSupplyRating)