def sortedListToBST(head):
    if head == None:
        return None
    if head.next == None:
        root = TreeNode(head.val)
        return root
    if head.next.next == None:
        root = TreeNode(head.next.val)
        root.left = TreeNode(head.val)
        return root
    temp = head
    length = 0
    while temp:
        length += 1
        temp = temp.next
    mid = length//2
    leftPtr = head
    midPtr = head
    i = 0
    while i < mid-1:
        midPtr = midPtr.next
        i += 1
    root = TreeNode(midPtr.next.val)
    rightPtr = midPtr.next.next
    midPtr.next = None
    root.left = sortedListToBST(leftPtr)
    root.right = sortedListToBST(rightPtr)
    return root
