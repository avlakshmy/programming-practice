def myPow(x, n):
    if n == 0:
        return 1

    if x == 1:
        return 1

    if x == -1:
        if n%2 == 0:
            return 1
        return -1

    if x == 0:
        return 0

    if n > 0:
        ans = 1
        while n > 0:
            ans = ans * x
            n -= 1
            if abs(ans) <= 0.000001:
                return 0
        return ans

    ans = 1
    n = -1 * n
    while n > 0:
        ans = ans/x
        n -= 1
        if abs(ans) <= 0.000001:
            return 0
    return ans
