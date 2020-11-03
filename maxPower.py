def maxPower(s):
    curr = s[0]
    maxlen = 1
    maxlens = []
    i = 1
    while i < len(s):
        if s[i] == curr:
            maxlen += 1
        else:
            maxlens.append(maxlen)
            curr = s[i]
            maxlen = 1
        i += 1
    maxlens.append(maxlen)
    return max(maxlens)
