def checkPerfectNumber(num):
    if num <= 1:
        return False
    count = 0
    sqrt = int(math.sqrt(num))
    i = 1
    while i <= sqrt:
        if num%i == 0:
            count += i
            count += (num//i)
        i += 1
    if count == 2*num:
        return True
    return False
