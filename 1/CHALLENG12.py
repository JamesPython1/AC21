data = [int(d) for d in open("input.txt", "r").read().splitlines()]

sums = []
for i in range(len(data)-2):
    total = 0
    for x in range(3): total+=data[i+x]
    print("total for that 3", total)
    sums.append(total)

increases = 0
for i in range(len(sums)):
    if (i != 0) and (sums[i] > sums[i-1]): increases+=1

print(increases)