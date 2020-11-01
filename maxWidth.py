def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
    x = [point[0] for point in points]
    x = list(set(x))
    x.sort()
    subs = []
    for i in range(1, len(x)):
        subs.append(x[i] - x[i-1])
    return max(subs)
