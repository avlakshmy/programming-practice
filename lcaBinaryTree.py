def getPathFromRootToNode(root, node):
    stack = []
    visited = set()
    stack.append(root)
    while len(stack) > 0:
        curr = stack[-1]
        if curr.val == node.val:
            break
        if curr.left and not curr.left.val in visited:
            stack.append(curr.left)
            continue
        elif curr.right and not curr.right.val in visited:
            stack.append(curr.right)
            continue
        visited.add(curr.val)
        stack.pop()
    return stack

def lowestCommonAncestor(root, p, q):
    path1 = getPathFromRootToNode(root, p)
    path2 = getPathFromRootToNode(root, q)
    i = 0
    j = 0
    while i < len(path1) and j < len(path2):
        if path1[i] == path2[j]:
            i += 1
            j += 1
        else:
            break
    return path1[i-1]
