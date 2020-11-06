def arrayManipulation(n, queries):
    arr = [0 for _ in range(n+2)]
    for a, b, k in queries:
        arr[a] += k
        arr[b+1] -= k
    result = acc = 0
    for x in arr:
        acc += x
        result = max(result, acc)
    return result
