def smallestDivisor(nums, threshold):
    mindiv = 1
    maxdiv = max(nums)
    while (mindiv <= maxdiv):
        div = (mindiv + maxdiv)//2
        sumval = 0
        for num in nums:
            sumval += (num//div)
            if not num%div == 0:
                sumval += 1
        if sumval > threshold:
            mindiv = div + 1
        else:
            maxdiv = div - 1
    return mindiv
