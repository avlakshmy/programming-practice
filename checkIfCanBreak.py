def canBreak(s, t):
    for i in range(len(s)):
        if ord(s[i]) < ord(t[i]):
            return False
    return True

def checkIfCanBreak(s1, s2):
    if canBreak(sorted(s1), sorted(s2)):
        return True
    elif canBreak(sorted(s2), sorted(s1)):
        return True
    return False
