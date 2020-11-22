class Node:
    def __init__(self, i, j):
        self.i = i
        self.j = j
        self.incomingEdges = []
        self.outgoingEdges = []
        self.score = 0        

def getBaldNodes(nodes):
    baldNodes = []
    for node in nodes:
        if len(nodes[node].incomingEdges) == 0:
            baldNodes.append(node)
    return baldNodes
        
def longestIncreasingPath(matrix):
    if len(matrix) == 0:
        return 0
    incomingEdges = {}
    outgoingEdges = {}
    rows = len(matrix)
    cols = len(matrix[0])
    nodes = {}
    for i in range(rows):
        for j in range(cols):
            mynode = Node(i, j)
            nodes[(i,j)] = mynode
    for i in range(rows):
        for j in range(cols):
            if i+1 <= rows-1 and matrix[i+1][j] > matrix[i][j]:
                nodes[(i,j)].outgoingEdges.append((i+1,j))
                nodes[(i+1,j)].incomingEdges.append((i,j))
            if i-1 >= 0 and matrix[i-1][j] > matrix[i][j]:
                nodes[(i,j)].outgoingEdges.append((i-1,j))
                nodes[(i-1,j)].incomingEdges.append((i,j))
            if j+1 <= cols-1 and matrix[i][j+1] > matrix[i][j]:
                nodes[(i,j)].outgoingEdges.append((i,j+1))
                nodes[(i,j+1)].incomingEdges.append((i,j))
            if j-1 >= 0 and matrix[i][j-1] > matrix[i][j]:
                nodes[(i,j)].outgoingEdges.append((i,j-1))
                nodes[(i,j-1)].incomingEdges.append((i,j))

    tempNodes = dict(nodes)
    baldNodes = getBaldNodes(tempNodes)
    while len(baldNodes) > 0:
        for node in baldNodes:
            for adj in tempNodes[node].outgoingEdges:
                if nodes[node].score + 1 > nodes[adj].score:
                    nodes[adj].score = nodes[node].score + 1
                tempNodes[adj].incomingEdges.remove(node)
        for node in baldNodes:
            del tempNodes[node]
        baldNodes = getBaldNodes(tempNodes)
    bestScore = -1
    for node in nodes:
        if nodes[node].score > bestScore:
            bestScore = nodes[node].score
    return bestScore+1
