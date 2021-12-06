import tqdm
from matplotlib import pyplot as plt # note: numpy difficult with 3.10 so using 3.9 interpreter
from celluloid import Camera

fig = plt.figure()
camera = Camera(fig)

coordData = open("input.txt", "r").read().splitlines()
startCoords, endCoords = [c.split(" -> ")[0].split(",") for c in coordData], [c.split(" -> ")[1].split(",") for c in coordData]
coordMap = {}

tPlts = []

for it in tqdm.tqdm(range(len(startCoords))): # tqdm prints nice progress bar btw.
    x1, x2 = int(startCoords[it][0]), int(endCoords[it][0])
    y1, y2 = int(startCoords[it][1]), int(endCoords[it][1])
    coords = []
    if x1 == x2:
        for i in range(abs(y2-y1)+1): coords.append((x1,y1-i)) if y1 > y2 else coords.append((x1,y1+i))
    elif y1 == y2:
        for i in range(abs(x2-x1)+1): coords.append((x1-i,y1)) if x1 > x2 else coords.append((x1+i,y1))
    # diagonals - presumed all other data
    else:
        xs, ys = [], []
        for i in range(abs(x2-x1)+1): # gap between x2 x1 and y2 y1 MUST be same
            xs.append(x1-i) if x1 > x2 else xs.append(x1 + i)
            ys.append(y1-i) if y1 > y2 else ys.append(y1 + i)
        coords = [(xs[i],ys[i]) for i in range(len(xs))]


    for coord in coords:
        if coord not in list(coordMap.keys()): coordMap[coord] = 1
        else: coordMap[coord] += 1

    tPlts.append(coords)
    if it%10==0:
        for t in tPlts: plt.plot([cord[0] for cord in t],[cord[1] for cord in t])
        camera.snap()

numberOfPlusTwo = sum([c for c in list(coordMap.values()) if c>=2])
print(numberOfPlusTwo)

animation = camera.animate()
animation.save('animation.mp4')