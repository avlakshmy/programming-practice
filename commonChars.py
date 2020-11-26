def commonChars(A):
    chars = list(set(''.join(A)))
    ans = []
    for ch in chars:
        counts = []
        for word in A:
            if ch in word:
                counts.append(word.count(ch))
            else:
                counts.append(0)
        minFreq = min(counts)
        if minFreq > 0:
            ans.extend([ch for _ in range(minFreq)])
    return ans
