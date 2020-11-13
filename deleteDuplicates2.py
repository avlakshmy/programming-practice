def deleteDuplicates(head):
    if head == None or head.next == None:
        return head
    currValue = head.val
    temp = head
    prev = ListNode()
    prev.next = head
    tempHead = prev
    while temp and temp.next:
        flag = 0
        while temp.next and temp.next.val == currValue:
            flag = 1
            temp.next = temp.next.next
        if flag == 1:
            if temp.next:
                currValue = temp.next.val
            prev.next = temp.next
            temp = temp.next

        elif temp.next:
            currValue = temp.next.val
            prev = temp
            temp = temp.next
    return tempHead.next
