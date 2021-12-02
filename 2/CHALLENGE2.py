commands = open("input.txt", "r").read().splitlines()

depth = 0
horizontal = 0

for c in commands:
    cParts = c.split(" ")
    if cParts[0] == "forward": horizontal += int(cParts[1])
    elif cParts[0] == "up": depth -= int(cParts[1])
    elif cParts[0] == "down": depth += int(cParts[1])
    print(depth, horizontal)

print(depth*horizontal)