def destCity(paths):
    outgoingEdges = {}

    for path in paths:
        if path[0] in outgoingEdges:
            outgoingEdges[path[0]].append(path[1])
        else:
            outgoingEdges[path[0]] = [path[1]]

        if not path[1] in outgoingEdges:
            outgoingEdges[path[1]] = []

    for city in outgoingEdges:
        if outgoingEdges[city] == []:
            return city
