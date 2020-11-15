def sumEvenGrandparent(root):
    if root == None:
        return 0
    if root.val % 2 == 1:
        return sumEvenGrandparent(root.left) + sumEvenGrandparent(root.right)
    count = 0
    if root.left:
        if root.left.left:
            count += root.left.left.val
        if root.left.right:
            count += root.left.right.val
    if root.right:
        if root.right.left:
            count += root.right.left.val
        if root.right.right:
            count += root.right.right.val
    return count + sumEvenGrandparent(root.left) + sumEvenGrandparent(root.right)
