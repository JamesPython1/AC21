coordData = open("input.txt", "r").read().splitlines()
startCoords = [c.split(" -> ")[0].split(",") for c in coordData]
endCoords = [c.split(" -> ")[1].split(",") for c in coordData]
coordMap = {}

for it in range(len(startCoords)):
    print(it)
    x1, x2 = int(startCoords[it][0]), int(endCoords[it][0])
    y1, y2 = int(startCoords[it][1]), int(endCoords[it][1])
    coords = []
    if x1 == x2:
        for i in range(abs(y2-y1)+1):
            if y1 > y2: coords.append((x1,y1-i))
            else: coords.append((x1,y1+i))
    if y1 == y2:
        for i in range(abs(x2-x1)+1):
            if x1 > x2: coords.append((x1-i,y1))
            else: coords.append((x1+i,y1))

    for coord in coords:
        if coord not in list(coordMap.keys()): coordMap[coord] = 1
        else: coordMap[coord] += 1

count = list(coordMap.values())
numberOfPlusTwo = 0
for c in count:
    if c >= 2: numberOfPlusTwo += 1

print(numberOfPlusTwo)