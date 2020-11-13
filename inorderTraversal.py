def inorderTraversal(root):
    if root == None:
        return []
    if root.left == None and root.right == None:
        return [root.val]
    inorderList = []
    if root.left:
        inorderList.extend(self.inorderTraversal(root.left))
    inorderList.append(root.val)
    if root.right:
        inorderList.extend(self.inorderTraversal(root.right))
    return inorderList
