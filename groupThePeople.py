def groupThePeople(groupSizes):
    groups = {}
    for i in range(len(groupSizes)):
        if groupSizes[i] in groups:
            groups[groupSizes[i]].append(i)
        else:
            groups[groupSizes[i]] = [i]
    ans = []
    for grpSz in groups:
        for i in range(0, len(groups[grpSz]), grpSz):
            ans.append(groups[grpSz][i:i+grpSz])
    return ans
