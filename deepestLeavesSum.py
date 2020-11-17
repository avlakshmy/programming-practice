def getHeight(root):
    if root == None:
        return 0
    return 1 + max(getHeight(root.left), getHeight(root.right))

def deepestLeavesSum(root):
    if root == None:
        return 0
    height = getHeight(root)
    queue = [root]
    i = 1
    while i < height:
        nextLevel = []
        for node in queue:
            if not node == None:
                nextLevel.append(node.left)
                nextLevel.append(node.right)
        queue[:] = nextLevel[:]
        i += 1
    value = 0
    for node in queue:
        if not node == None:
            value += node.val
    return value
