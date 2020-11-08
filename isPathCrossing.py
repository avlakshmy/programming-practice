def isPathCrossing(path):
    visited = set()
    start = (0,0)
    visited.add(start)
    for direction in path:
        if direction == 'N':
            start = (start[0], start[1] + 1)
        elif direction == 'S':
            start = (start[0], start[1] - 1)
        elif direction == 'E':
            start = (start[0] + 1, start[1])
        else:
            start = (start[0] - 1, start[1])
        if start in visited:
            return True
        else:
            visited.add(start)
    return False
