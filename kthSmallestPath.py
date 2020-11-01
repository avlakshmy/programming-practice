def kthSmallestPath(self, destination: List[int], k: int) -> str:
    h = destination[1]
    v = destination[0]

    ncr = [[0 for _ in range(v+1)] for _ in range(h+v+1)]
    for n in range(0,h+v+1):
        ncr[n][0] = 1
    for n in range(1, h+v+1):
        for r in range(1,v+1):
            ncr[n][r] = ncr[n-1][r] + ncr[n-1][r-1]   

    instruction = []
    remDown = v
    for i in range(h + v):
        remSteps = h + v - (i + 1)
        com = ncr[remSteps][remDown]
        if com >= k:
            instruction.append("H")
        else:
            remDown -= 1
            k -= com
            instruction.append("V")

    return ''.join(instruction)
