def isValidSudoku(board):
    nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    # checking rows
    for i in range(9):
        row = board[i]
        # print("row", row)
        for num in nums:
            if num in row and row.count(num) >= 2:
                return False 

    # checking columns
    for j in range(9):
        col = []
        for i in range(9):
            col.append(board[i][j])
        # print("col", col)
        for num in nums:
            if num in col and col.count(num) >= 2:
                return False

    # checking boxes
    starts = [(0,0), (0,3), (0,6), (3,0), (3,3), (3,6), (6,0), (6,3), (6,6)]
    for start in starts:
        box = []
        for i in range(start[0], start[0] + 3):
            for j in range(start[1], start[1] + 3):
                box.append(board[i][j])
        # print("box", box)
        for num in nums:
            if num in box and box.count(num) >= 2:
                return False

    return True
