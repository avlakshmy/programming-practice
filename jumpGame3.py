def canReach(arr, start):
    low = 0
    high = len(arr) - 1
    queue = [start]
    visited = set()
    while len(queue) > 0:
        currIndex = queue[0]
        queue.remove(currIndex)
        visited.add(currIndex)
        if arr[currIndex] == 0:
            return True
        next1 = currIndex + arr[currIndex]
        if not (next1 in visited) and next1 <= high:
            queue.append(next1)
        next2 = currIndex - arr[currIndex]
        if not (next2 in visited) and next2 >= 0:
            queue.append(next2)
    return False
