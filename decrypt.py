def decrypt(code, k):
    if k == 0:
        return [0 for _ in range(len(code))]
    if k < 0:
        k = -1 * k
        sums = []
        sums.append(sum([code[(len(code)-i)%len(code)] for i in range(1,k+1)]))
        for i in range(1, len(code)):
            sums.append(sums[-1] - code[(len(code)-(k-i+1))%len(code)] + code[(i-1)%len(code)])
        return sums
    sums = []
    sums.append(sum([code[i%len(code)] for i in range(1, k+1)]))
    for i in range(1, len(code)):
        sums.append(sums[-1] - code[i%len(code)] + code[(k+i)%len(code)])
    return sums
