def isMirror(root1, root2):
    if root1 == None and root2 == None:
        return True
    if root1 == None:
        return False
    if root2 == None:
        return False
    if not root1.val == root2.val:
        return False
    return isMirror(root1.left, root2.right) and isMirror(root1.right, root2.left)

def isSymmetric(root):
    if root == None:
        return True
    if root.left == None and root.right == None:
        return True
    if root.left == None:
        return False
    if root.right == None:
        return False
    if not root.left.val == root.right.val:
        return False
    return isMirror(root.left, root.right)
