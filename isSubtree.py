def isSameTree(p, q):
    if p == None and q == None:
        return True
    if p == None or q == None:
        return False
    return (p.val == q.val) and isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

def isSubtree(s, t):
    if s == None:
        return False
    if isSameTree(s, t) == True:
        return True
    leftSub = isSubtree(s.left, t)
    rightSub = isSubtree(s.right, t)
    if leftSub or rightSub:
        return True
    return False
