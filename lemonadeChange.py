def lemonadeChange(bills):
    myChange = {}
    myChange[5] = 0
    myChange[10] = 0
    myChange[20] = 0
    for bill in bills:
        if bill == 5:
            myChange[5] += 1
        elif bill == 10:
            if myChange[5] >= 1:
                myChange[5] -= 1
                myChange[10] += 1
            else:
                return False
        else:
            if myChange[5] >= 1 and myChange[10] >= 1:
                myChange[5] -= 1
                myChange[10] -= 1
                myChange[20] += 1
            elif myChange[5] >= 3:
                myChange[5] -= 3
                myChange[20] += 1
            else:
                return False
    return True
