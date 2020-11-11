def isHappy(n):
    found = set()
    while True:
        newN = sum([int(x)*int(x) for x in str(n)])
        if newN == 1:
            return True
        if not newN in found:
            found.add(newN)
            n = newN
        else:
            return False
