def removeZeroSumSublists(self, head: ListNode) -> ListNode:
    if head == None:
        return None
    arr = []
    while head:
        arr.append(head.val)
        head = head.next
    i = 0
    while len(arr) > 0 and i < len(arr):
        j = i
        while len(arr) > 0 and j < len(arr):
            flag = 0
            if sum(arr[i:j+1]) == 0:
                x = j-i+1
                while x > 0:
                    arr.pop(i)
                    x -= 1
                flag = 1
                j -= 1
            j += 1
            if flag == 1:
                i = -1
                break
        i += 1

    if len(arr) > 0:
        head = ListNode(arr[0])
        prev = head
        for i in range(1, len(arr)):
            curr = ListNode(arr[i])
            prev.next = curr
            prev = curr
        return head
