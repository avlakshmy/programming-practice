def hIndex(citations):
    if len(citations) == 0:
        return 0
    citations.sort()
    h = min(citations[-1], 1)
    for i in range(1, len(citations)):
        h = max(h, min(i+1, citations[len(citations)-i-1]))
    return h
