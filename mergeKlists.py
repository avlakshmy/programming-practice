def mergeKLists(lists):
    k = len(lists)
    if k == 0:
        return None
    if k == 1:
        return lists[0]
    ptrs = [lists[i] for i in range(k)]
    while None in ptrs:
        ptrs.remove(None)
    ll = ListNode()
    llHead = ll
    while len(ptrs) > 0:
        values = [ptrs[i].val for i in range(len(ptrs))]
        minVal = min(values)
        ll.next = ListNode(minVal)
        ll = ll.next
        minIndex = values.index(minVal)
        ptrs[minIndex] = ptrs[minIndex].next
        while None in ptrs:
            ptrs.remove(None)
    return llHead.next
