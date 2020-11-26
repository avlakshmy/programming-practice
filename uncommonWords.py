def uncommonFromSentences(A, B):
    A = A.split()
    B = B.split()
    set1 = set(A)
    set2 = set(B)
    ans = list((set1 - set2) | (set2 - set1))
    ans2 = []
    for word in ans:
        if word in A:
            if A.count(word) == 1:
                ans2.append(word)
        else:
            if B.count(word) == 1:
                ans2.append(word)
    return ans2
