def canFormArray(arr, pieces):
    if len(pieces) == 0:
        return True
    p = pieces[0]
    if len(p) == 1:
        if p[0] in arr:
            arr.remove(p[0])
            pieces.remove(p)
            return canFormArray(arr, pieces)
        else:
            return False
    else:
        pi = 0
        ai = 0
        while ai < len(arr) and not (arr[ai] == p[pi]):
            ai += 1
        start = ai
        while ai < len(arr) and pi < len(p) and arr[ai] == p[pi]:
            ai += 1
            pi += 1
        if pi == len(p):
            arr[:] = arr[:start] + arr[start+len(p):]
            pieces.remove(p)
            return canFormArray(arr, pieces)
        else:
            return False
