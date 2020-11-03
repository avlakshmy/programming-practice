def canPlaceFlowers(flowerbed, n):
    leftover = n
    if len(flowerbed) == 1:
        if flowerbed[0] == 0 and n == 1:
            return True
        elif n == 0:
            return True
        else:
            return False
    i = 0
    while i < len(flowerbed):
        if flowerbed[i] == 0:
            if i >= 1 and i <= len(flowerbed) - 2:
                if flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                    flowerbed[i] = 1
                    leftover -= 1
            else:
                if i >= 1 and flowerbed[i-1] == 0:
                    flowerbed[i] = 1
                    leftover -= 1
                elif i <= len(flowerbed) - 2 and flowerbed[i+1] == 0:
                    flowerbed[i] = 1
                    leftover -= 1                    
        i += 1
    if leftover > 0:
        return False
    return True
