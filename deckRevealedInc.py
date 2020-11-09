def deckRevealedIncreasing(deck):
    deck.sort()
    l = len(deck)
    if l <= 2:
        return deck
    half = l//2
    if l % 2 == 1:
        half += 1
    firstPart = deck[:half] 
    arr = self.deckRevealedIncreasing(deck[half:])
    if l % 2 == 1:
        arr = ([arr[-1]] + arr[:-1])
    ans = []
    f = 0
    s = 0
    for i in range(l):
        if i%2 == 0 and f < len(firstPart):
            ans.append(firstPart[f])
            f += 1
        else:
            ans.append(arr[s])
            s += 1
    return ans
