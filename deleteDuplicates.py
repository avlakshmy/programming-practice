def deleteDuplicates(head):
    if head == None or head.next == None:
        return head
    currValue = head.val
    temp = head
    while temp.next:
        while temp.next and temp.next.val == currValue:
            temp.next = temp.next.next
        if temp.next:
            currValue = temp.next.val
            temp = temp.next
    return head
