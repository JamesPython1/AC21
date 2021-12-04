import matplotlib.pyplot as plt

commands = open("input.txt", "r").read().splitlines()

depth = 0
aim = 0
horizontal = 0

for c in commands:
    cParts = c.split(" ")
    plt.plot()
    if cParts[0] == "forward":
        horizontal += int(cParts[1])
        depth += aim * int(cParts[1])
    elif cParts[0] == "up":
        aim -= int(cParts[1])
    elif cParts[0] == "down":
        aim += int(cParts[1])


print(depth*horizontal)