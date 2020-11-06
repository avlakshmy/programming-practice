def isIsomorphic(s, t):
    mapping1 = {}
    count1 = 0
    for ch in s:
        if not ch in mapping1:
            mapping1[ch] = count1
            count1 += 1
    transformed_s = [mapping1[ch] for ch in s]

    mapping2 = {}
    count2 = 0
    for ch in t:
        if not ch in mapping2:
            mapping2[ch] = count2
            count2 += 1
    transformed_t = [mapping2[ch] for ch in t]

    if transformed_s == transformed_t:
        return True

    return False
