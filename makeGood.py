def makeGood(s):
    i = 0
    s = list(s)
    while (i < len(s) - 1):
        if abs(ord(s[i]) - ord(s[i+1])) == 32:
            s.pop(i)
            s.pop(i)
            i = 0
        else:
            i += 1
    return ''.join(s)
