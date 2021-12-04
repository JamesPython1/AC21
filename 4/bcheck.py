board = [
['22', '13', '*', '*', '*'],
['8', '*', '*', '*', '*'],
['*', '*', '*', '*', '*'],
['6', '*', '3', '18', '*'],
['1', '12', '20', '15', '19']

]

aRow, aColumn = False, False
for r in range(len(board)):
    aRow = board[r].count(board[r][0]) == len(board[r])
    if aRow: break

# sort columns into array
columns = []
for c in range(len(board[0])):
    cl = []
    for r in range(len(board)): cl.append(board[r][c])
    columns.append(cl)

for r in range(len(columns)):
    aColumn = columns[r].count(columns[r][0]) == len(columns[r])
    if aColumn: break


print(aRow or aColumn)