def countCharacters(words, chars):
    charFreq = {}
    for ch in chars:
        if ch in charFreq:
            charFreq[ch] += 1
        else:
            charFreq[ch] = 1

    ans = 0
    for word in words:
        wordFreq = {}
        for ch in word:
            if ch in wordFreq:
                wordFreq[ch] += 1
            else:
                wordFreq[ch] = 1
        flag = True
        for ch in wordFreq:
            if not(ch in charFreq and wordFreq[ch] <= charFreq[ch]):
                flag = False
                break
        if flag == True:
            ans += len(word)

    return ans
