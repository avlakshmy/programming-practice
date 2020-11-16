def binaryTreePaths(root):
    if root == None:
        return []
    if root.left == None and root.right == None:
        return [str(root.val)]
    leftPaths = binaryTreePaths(root.left)
    rightPaths = binaryTreePaths(root.right)
    allPaths = []
    for path in leftPaths:
        allPaths.append('{}->{}'.format(root.val, path))
    for path in rightPaths:
        allPaths.append('{}->{}'.format(root.val, path))
    return allPaths
