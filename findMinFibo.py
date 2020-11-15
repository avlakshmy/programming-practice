def findMinFibonacciNumbers(k):
    if k < 2: 
        return k
        
    fibo = [1,1]
    while(fibo[-1] <= k):
        fibo.append(fibo[-1] + fibo[-2])    

    ans = 0
    i = len(fibo) - 1
    while i >= 0:
        if fibo[i] <= k:
            break
        i -= 1

    return 1 + findMinFibonacciNumbers(k-fibo[i])
