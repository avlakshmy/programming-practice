def postOrder(root, diffs):
    if root == None:
        return [0,0]
    if root.left == None and root.right == None:
        return [root.val, root.val]
    if root.left:
        leftVals = postOrder(root.left, diffs)
    else:
        leftVals = [root.val, root.val]
    if root.right:
        rightVals = postOrder(root.right, diffs)
    else:
        rightVals = [root.val, root.val]
    rootVals = [min(leftVals[0], rightVals[0], root.val), max(leftVals[1], rightVals[1], root.val)]
    diffs.append(abs(root.val - rootVals[0]))
    diffs.append(abs(root.val - rootVals[1]))
    return rootVals

def maxAncestorDiff(root):
    diffs = []
    postOrder(root, diffs)
    return max(diffs)
