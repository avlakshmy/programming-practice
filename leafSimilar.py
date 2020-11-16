def getLeafValueSequence(root):
    if root == None:
        return []
    if root.left == None and root.right == None:
        return [root.val]
    leafValueSeq = []
    leafValueSeq.extend(getLeafValueSequence(root.left))
    leafValueSeq.extend(getLeafValueSequence(root.right))
    return leafValueSeq

def leafSimilar(root1, root2):
    lvs1 = getLeafValueSequence(root1)
    lvs2 = getLeafValueSequence(root2)
    if lvs1 == lvs2:
        return True
    return False
