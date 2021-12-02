data = [int(d) for d in open("input.txt", "r").read().splitlines()]

increases = 0
for i in range(len(data)):
    if i != 0:
        if data[i] > data[i-1]: increases+=1

print(increases)
