def isSelfDividing(num):
    digits = [int(x) for x in list(str(num))]
    for digit in digits:
        if digit == 0:
            return False
        if not(num % digit == 0):
            return False
    return True
    
def selfDividingNumbers(left, right):
    ans = []
    for num in range(left, right+1):
        if isSelfDividing(num):
            ans.append(num)
    return ans
