def inorderTraversal(root):
    if root == None:
        return []
    inorder = []
    inorder.extend(inorderTraversal(root.left))
    inorder.append(root.val)
    inorder.extend(inorderTraversal(root.right))
    return inorder

def increasingBST(root):
    inorder = inorderTraversal(root)
    newRoot = TreeNode(inorder[0])
    prevNode = newRoot
    for i in range(1, len(inorder)):
        newNode = TreeNode(inorder[i])
        prevNode.right = newNode
        prevNode = newNode
    return newRoot
