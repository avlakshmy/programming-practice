def merge(intervals):
    if len(intervals) <= 1:
        return intervals
    ans = []
    temp = intervals[:]
    temp.sort(reverse=True, key=lambda x: x[0])
    prev = temp.pop()
    while len(temp) > 0:
        curr = temp.pop()
        if prev[1] >= curr[0]:
            prev = [prev[0], max(prev[1],curr[1])]
        else:
            ans.append(prev)
            prev = curr[:]
    if not prev in ans:
        ans.append(prev)
    return ans
