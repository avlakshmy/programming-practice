def maxScore(s):
    if s[0] == '0':
        left = [1]
        right = [s[1:].count('1')]
    else:
        left = [0]
        right = [s[1:].count('1')]
    for i in range(1,len(s)-1):
        if s[i] == '0':
            left.append(left[-1] + 1)
            right.append(right[-1])
        else:
            left.append(left[-1])
            right.append(right[-1] - 1)
    score = [l + r for l,r in zip(left,right)]
    return max(score)
