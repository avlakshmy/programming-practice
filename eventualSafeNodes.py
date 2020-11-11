def eventualSafeNodes(graph):
    n = len(graph)
    incomingEdges = dict(zip(list(range(n)), [[] for _ in range(n)]))
    outgoingEdges = dict(zip(list(range(n)), [[] for _ in range(n)]))
    for v1 in range(n):
        outgoingEdges[v1].extend(graph[v1])
        for v2 in graph[v1]:
            incomingEdges[v2].append(v1)
    safeVertices = []
    numIncomingZero = len([v for v in outgoingEdges if outgoingEdges[v] == []])
    while numIncomingZero > 0:
        for v in range(n):
            if v in outgoingEdges and len(outgoingEdges[v]) == 0:
                safeVertices.append(v)
                del outgoingEdges[v]
                if v in incomingEdges:
                    for u in incomingEdges[v]:
                        if u in outgoingEdges:
                            outgoingEdges[u].remove(v)
                    del incomingEdges[v]
        numIncomingZero = len([v for v in outgoingEdges if outgoingEdges[v] == []])
    safeVertices.sort()
    return safeVertices
