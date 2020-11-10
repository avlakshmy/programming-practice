def tribonacci(N):
    if N == 0:
        return 0
    if N == 1:
        return 1
    if N == 2:
        return 1
    tribo = [0,1,1]
    for i in range(3, N+1):
        tribo.append(tribo[-1]+tribo[-2]+tribo[-3])
    return tribo[-1]
