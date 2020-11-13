import math
def isValidBSTUtil(root, minVal, maxVal):
    if root == None:
        return True
    if root.val <= minVal or root.val >= maxVal:
        return False
    return isValidBSTUtil(root.left, minVal, root.val) and isValidBSTUtil(root.right, root.val, maxVal)

def isValidBST(root):
    return isValidBSTUtil(root, -math.inf, math.inf)
