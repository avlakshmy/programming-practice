def getPaths(source, graph):
    if graph[source] == []:
        return [[source]]
    paths = []
    for outgoing in graph[source]:
        temp = getPaths(outgoing, graph)
        for x in temp:
            paths.append([source] + x)
    return paths

def allPathsSourceTarget(graph):
    ans = getPaths(0, graph)
    n = len(graph)
    sourceToTargetPaths = []
    for i in range(len(ans)):
        if n-1 in ans[i]:
            targetInd = ans[i].index(n-1)
            sourceToTargetPaths.append(ans[i][:targetInd+1])
    return sourceToTargetPaths
        
