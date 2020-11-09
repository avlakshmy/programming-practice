def tictactoe(moves):
    grid = [[" " for _ in range(3)] for _ in range(3)]
    for i in range(len(moves)):
        if i%2 == 0:
            grid[moves[i][0]][moves[i][1]] = 'X'
        else:
            grid[moves[i][0]][moves[i][1]] = 'O'

    if grid[0] == ['X','X','X'] or grid[1] == ['X','X','X'] or grid[2] == ['X','X','X']:
        return 'A'
    if grid[0] == ['O','O','O'] or grid[1] == ['O','O','O'] or grid[2] == ['O','O','O']:
        return 'B'

    transpose = list(zip(*grid))

    if transpose[0] == ('X','X','X') or transpose[1] == ('X','X','X') or transpose[2] == ('X','X','X'):
        return 'A'
    if transpose[0] == ('O','O','O') or transpose[1] == ('O','O','O') or transpose[2] == ('O','O','O'):
        return 'B'

    if grid[0][0] == 'X' and grid[1][1] == 'X' and grid[2][2] == 'X':
        return 'A'
    if grid[0][2] == 'X' and grid[1][1] == 'X' and grid[2][0] == 'X':
        return 'A'

    if grid[0][0] == 'O' and grid[1][1] == 'O' and grid[2][2] == 'O':
        return 'B'
    if grid[0][2] == 'O' and grid[1][1] == 'O' and grid[2][0] == 'O':
        return 'B'

    if len(moves) == 9:
        return "Draw"

    return "Pending"
