def buildTree(inorder, postorder):
    if len(inorder) == 0 or len(postorder) == None:
        return None
    rootVal = postorder.pop()
    rootIndex = inorder.index(rootVal)
    root = TreeNode(rootVal)
    rightChildRoot = self.buildTree(inorder[rootIndex+1:], postorder)
    leftChildRoot = self.buildTree(inorder[:rootIndex], postorder)
    root.left = leftChildRoot
    root.right = rightChildRoot
    return root
