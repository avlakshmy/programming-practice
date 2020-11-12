def countPrimes(n):
    if n <= 1:
        return 0
    isPrime = [True for _ in range(n)]
    isPrime[0] = False
    isPrime[1] = False
    for i in range(2,n):
        if isPrime[i] == True:
            j = 2*i
            while j < n:
                isPrime[j] = False
                j += i
    return isPrime.count(True)
