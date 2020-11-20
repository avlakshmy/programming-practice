def getBaldNodes(incomingEdges):
    baldNodes = []
    for node in incomingEdges:
        if len(incomingEdges[node]) == 0:
            baldNodes.append(node)
    return baldNodes

def findOrder(numCourses, prerequisites):
    outgoingEdges = {}
    incomingEdges = {}
    for i in range(numCourses):
        outgoingEdges[i] = []
        incomingEdges[i] = []
    for edge in prerequisites:
        u = edge[1]
        v = edge[0]
        outgoingEdges[u].append(v)
        incomingEdges[v].append(u)
    toposort = []
    baldNodes = getBaldNodes(incomingEdges)
    while len(baldNodes) > 0:
        toposort.extend(baldNodes)
        for node in baldNodes:
            for out in outgoingEdges[node]:
                incomingEdges[out].remove(node)
            del incomingEdges[node]
            del outgoingEdges[node]
        baldNodes = getBaldNodes(incomingEdges) 
    if len(toposort) == numCourses:
        return toposort
    return []
