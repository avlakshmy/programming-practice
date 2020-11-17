def invert(S):
    ans = ""
    for s in S:
        if s == '1':
            ans += '0'
        else:
            ans += '1'
    return ans
    
def findKthBit(n, k):
    S = [None]
    S.append('0')
    for i in range(2, n+1):
        S.append(S[-1] + '1' + invert(S[-1])[::-1])
    return S[n][k-1]
