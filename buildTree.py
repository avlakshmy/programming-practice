def buildTree(preorder, inorder):
    if len(inorder) == 0:
        return None
    rootVal = preorder.pop(0)
    rootIndex = inorder.index(rootVal)
    root = TreeNode(rootVal)
    leftChildRoot = self.buildTree(preorder, inorder[:rootIndex])
    rightChildRoot = self.buildTree(preorder, inorder[rootIndex+1:])
    root.left = leftChildRoot
    root.right = rightChildRoot
    return root
