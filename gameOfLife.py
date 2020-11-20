def numLiveNeighbours(board, i, j):
    rows = len(board)
    cols = len(board[0])
    numLive = 0
    if i+1 < rows:
        if board[i+1][j] == 1 or board[i+1][j] == -1:
            numLive += 1
        if j-1 >= 0:
            if board[i+1][j-1] == 1 or board[i+1][j-1] == -1:
                numLive += 1
        if j+1 < cols:
            if board[i+1][j+1] == 1 or board[i+1][j+1] == -1:
                numLive += 1
    if i-1 >= 0:
        if board[i-1][j] == 1 or board[i-1][j] == -1:
            numLive += 1
        if j-1 >= 0:
            if board[i-1][j-1] == 1 or board[i-1][j-1] == -1:
                numLive += 1
        if j+1 < cols:
            if board[i-1][j+1] == 1 or board[i-1][j+1] == -1:
                numLive += 1
    if j-1 >= 0:
        if board[i][j-1] == 1 or board[i][j-1] == -1:
            numLive += 1
    if j+1 < cols:
        if board[i][j+1] == 1 or board[i][j+1] == -1:
            numLive += 1
            
    return numLive

def numDeadNeighbours(board, i, j):
    rows = len(board)
    cols = len(board[0])
    numDead = 0
    if i+1 < rows:
        if board[i+1][j] == 0 or board[i+1][j] == 2:
            numDead += 1
        if j-1 >= 0:
            if board[i+1][j-1] == 0 or board[i+1][j-1] == 2:
                numDead += 1
        if j+1 < cols:
            if board[i+1][j+1] == 0 or board[i+1][j+1] == 2:
                numDead += 1
    if i-1 >= 0:
        if board[i-1][j] == 0 or board[i-1][j] == 2:
            numDead += 1
        if j-1 >= 0:
            if board[i-1][j-1] == 0 or board[i-1][j-1] == 2:
                numDead += 1
        if j+1 < cols:
            if board[i-1][j+1] == 0 or board[i-1][j+1] == 2:
                numDead += 1
    if j-1 >= 0:
        if board[i][j-1] == 0 or board[i][j-1] == 2:
            numDead += 1
    if j+1 < cols:
        if board[i][j+1] == 0 or board[i][j+1] == 2:
            numDead += 1
            
    return numDead

def gameOfLife(board):
    rows = len(board)
    cols = len(board[0])
    for i in range(rows):
        for j in range(cols):
            numLive = numLiveNeighbours(board, i, j)
            numDead = numDeadNeighbours(board, i, j)
            if board[i][j] == 0 or board[i][j] == 2: # this cell is dead
                if numLive == 3:
                    board[i][j] = 2
            else: # this cell is living
                if numLive < 2 or numLive > 3:
                    board[i][j] = -1
    for i in range(rows):
        for j in range(cols):
            if board[i][j] == 2:
                board[i][j] = 1
            if board[i][j] == -1:
                board[i][j] = 0
