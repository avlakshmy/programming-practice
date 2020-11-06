def numJewelsInStones(J, S):
    isJewel = [False for _ in range(52)]
    for jewel in J:
        if ord(jewel) >= ord('a') and ord(jewel) <= ord('z'):
            index = ord(jewel) - ord('a')
        else:
            index = ord(jewel) - ord('A') + 26
        isJewel[index] = True
    count = 0
    for stone in S:
        if ord(stone) >= ord('a') and ord(stone) <= ord('z'):
            index = ord(stone) - ord('a')
        else:
            index = ord(stone) - ord('A') + 26
        if isJewel[index]:
            count += 1

    return count
