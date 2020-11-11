def removeElements(head, val):
    if head == None:
        return None
    prev = head
    while head and head.val == val:
        prev = head
        head = head.next
    temp = head
    while temp:
        if temp.val == val:
            if temp.next:
                temp.val = temp.next.val
                temp.next = temp.next.next
                temp = prev
            else:
                prev.next = None
        prev = temp
        temp = temp.next
    return head
