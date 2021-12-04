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

print(int(gamma,2)*int(epsilon,2))