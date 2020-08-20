def gcd(a, b):
    if a > b:
        a, b = b, a
    if a == 0:
        return b
    return gcd(b % a, a)

T = int(input())

for i in range(T):
    nl = [int(x) for x in input().split()]
    N = nl[0]
    L = nl[1]
    vals = [int(x) for x in input().split()]
    codes = [0 for _ in range(L+1)]

    for j in range(L-1):
        if not(vals[j] == vals[j+1]):
            codes[j+1] = gcd(vals[j], vals[j+1])
            for k in range(j, -1, -1):
                codes[k] = vals[k]//codes[k+1]
            for k in range(j+1, L):
                codes[k+1] = vals[k]//codes[k]

    crypt = list(set(codes))
    crypt.sort()

    message = ""
    for c in codes:
        ind = crypt.index(c)
        message += chr(ord('A') + ind)

    print("Case #{}: {}".format(i+1, message))
