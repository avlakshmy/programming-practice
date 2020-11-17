def nAryLevelOrder(root):
    if root == None:
        return []
    levelOrder = []
    queue = [root]
    while len(queue) > 0:
        levelOrder.append([node.val for node in queue])
        nextLevel = []
        for node in queue:
            if not node == None:
                for ch in node.children:
                    nextLevel.append(ch)
        queue[:] = nextLevel[:]
    return levelOrder
