# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def isStrictlyIncreasing(arr):
    if len(arr) == 1:
        return True
    for i in range(1, len(arr)):
        if arr[i] - arr[i-1] <= 0:
            return False
    return True

def isStrictlyDecreasing(arr):
    if len(arr) == 1:
        return True
    for i in range(1, len(arr)):
        if arr[i] - arr[i-1] >= 0:
            return False
    return True

def isEvenOddTree(root):
    level = 0
    queue = [root]
    while len(queue) > 0:
        curr = queue[:]
        if level%2 == 0:
            if not (all([x.val%2 == 1 for x in curr]) and isStrictlyIncreasing([x.val for x in curr])):
                return False
        if level%2 == 1:
            if not (all([x.val%2 == 0 for x in curr]) and isStrictlyDecreasing([x.val for x in curr])):
                return False
        children = []
        for node in curr:
            if node.left:
                children.append(node.left)
            if node.right:
                children.append(node.right)
        queue[:] = children[:]
        level += 1
    return True
