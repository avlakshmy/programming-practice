def addTwoNumbers(l1, l2):
    num1 = 0
    while l1:
        num1 = (num1 * 10) + l1.val
        l1 = l1.next
    num2 = 0
    while l2:
        num2 = (num2 * 10) + l2.val
        l2 = l2.next
    ans = num1 + num2
    digit = ans%10
    prev = ListNode(digit)
    ans = ans//10
    while ans:
        digit = ans%10
        curr = ListNode(digit)
        curr.next = prev
        prev = curr
        ans = ans//10
    return prev
