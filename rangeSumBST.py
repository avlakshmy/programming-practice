def inorderTraversal(root):
    if root == None:
        return []
    ans = []
    ans.extend(inorderTraversal(root.left))
    ans.append(root.val)
    ans.extend(inorderTraversal(root.right))
    return ans

def rangeSumBST(root, low, high):
    inorder = inorderTraversal(root)
    sumVal = 0
    i = 0
    while i < len(inorder):
        if inorder[i] >= low:
            break
        i += 1
    while i < len(inorder):
        if inorder[i] <= high:
            sumVal += inorder[i]
            i += 1
        else:
            break
    return sumVal
