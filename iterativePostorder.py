def postorder(root):
    if root == None:
        return []
    stack = []
    postorder = []
    stack.append(root)
    visited = set()
    visited.add(root)
    while len(stack) > 0:
        curr = stack[-1]
        currCh = curr.children[::-1]
        if len(currCh) > 0:
            chToVisit = [not ch in visited for ch in currCh]
            if any(chToVisit):
                for i in range(len(currCh)):
                    if chToVisit[i]:
                        visited.add(currCh[i])
                        stack.append(currCh[i])
            else:
                stack.pop()
                postorder.append(curr.val)
        else:
            stack.pop()
            postorder.append(curr.val)
    return postorder
