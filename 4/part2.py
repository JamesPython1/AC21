def checkBingo(board):
    aRow, aColumn = False, False
    columns = [[board[r][c] for r in range(len(board))] for c in range(len(board[0]))]  # sort columns into separate arrays

    for r in range(len(board)):
        aRow = board[r].count(board[r][0]) == len(board[r])
        if aRow: break

    for r in range(len(columns)):
        aColumn = columns[r].count(columns[r][0]) == len(columns[r])
        if aColumn: break

    return (aRow or aColumn)

numbersToCall = [26,55,7,40,56,34,58,90,60,83,37,36,9,27,42,19,46,18,49,52,75,17,70,41,12,78,15,64,50,54,2,77,76,10,43,79,22,32,47,0,72,30,21,82,6,95,13,59,16,89,1,85,57,62,81,38,29,80,8,67,20,53,69,25,23,61,86,71,68,98,35,31,4,33,91,74,14,28,65,24,97,88,3,39,11,93,66,44,45,96,92,51,63,84,73,99,94,87,5,48]

bingoData = open("input.txt", "r").read().splitlines()
boards = []
brd = []
for i in range(len(bingoData)):
    if bingoData[i] == "":
        boards.append(brd)
        brd = []
    elif bingoData[i]==bingoData[-1]:
        brd.append([c for c in bingoData[i].split(" ") if c != ""])
        boards.append(brd)
    else: brd.append([c for c in bingoData[i].split(" ") if c != ""])

forbiddenIndices, winningCallPos = [], [0 for i in range(len(boards))]

for i, numCalled in enumerate(numbersToCall):
    # apply bingo call to each board
    for it in range(len(boards)):
        if it not in forbiddenIndices:
            for r, _ in enumerate(boards[it]):
                for c, _ in enumerate(boards[it][r]):
                    if boards[it][r][c] == str(numCalled):
                        boards[it][r][c] = "*"
                        winningCallPos[it] = i
            if checkBingo(boards[it]): forbiddenIndices.append(it) # check board - prevent it from winning again

# output winning board details
lastToWinIndex, lastToWinNumCalled = winningCallPos.index(max(winningCallPos)), numbersToCall[max(winningCallPos)]
lastToWinBoard = boards[lastToWinIndex]
for line in lastToWinBoard: print(line)

# perform calculation to get score
total = 0
for r in range(len(lastToWinBoard)):
    for c in range(len(lastToWinBoard[r])):
        if lastToWinBoard[r][c] != "*": total += int(lastToWinBoard[r][c])

fScore = total * lastToWinNumCalled
print("final score", fScore)
