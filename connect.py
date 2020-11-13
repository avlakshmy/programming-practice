def connect(root):
    if root == None:
        return None
    queue = []
    queue.append(root)
    while len(queue) > 0:
        currLevel = []
        for top in queue:
            if top.left:
                currLevel.append(top.left)
            if top.right:
                currLevel.append(top.right)
        for i in range(len(currLevel) - 1):
            currLevel[i].next = currLevel[i+1]
        queue = []
        queue.extend(currLevel)
    return root
