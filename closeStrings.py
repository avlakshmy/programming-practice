def closeStrings(word1, word2):
    if not len(word1) == len(word2):
        return False

    freq1 = {}
    for ch in word1:
        if ch in freq1:
            freq1[ch] += 1
        else:
            freq1[ch] = 1

    freq2 = {}
    for ch in word2:
        if ch in freq2:
            freq2[ch] += 1
        else:
            freq2[ch] = 1


    if not set(freq1.keys()) == set(freq2.keys()):
        return False

    if not (sorted(freq1.values()) == sorted(freq2.values())):
        return False

    return True
