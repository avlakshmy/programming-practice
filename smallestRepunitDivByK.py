def smallestRepunitDivByK(K):
    rems = set()
    N = 1
    while True:
        rem = N % K
        if rem == 0:
            return len(str(N))
        if rem in rems:
            return -1
        rems.add(rem)
        N = N*10 + 1
