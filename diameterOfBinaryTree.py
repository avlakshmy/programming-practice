def getHeight(root):
    if root == None:
        return 0
    return 1 + max(getHeight(root.left), getHeight(root.right))

def getDiameter(root):
    if root == None:
        return 0
    l = getHeight(root.left)
    r = getHeight(root.right)
    ld = getDiameter(root.left)
    rd = getDiameter(root.right)
    return max(ld, rd, l + r + 1) 

def diameterOfBinaryTree(root):
    if root == None:
        return 0
    return getDiameter(root) - 1
