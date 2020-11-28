class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head):
    if not head == None and not head.next == None:
        revTail = head.next
        revHead = reverseList(head.next)
        revTail.next = head
        head.next = None
        return revHead

def reverse(arr):
    head = arr[0]
    revHead = reverseList(head)
    arr[:] = arr[::-1]

def getNumNodes(head):
    if head == None:
        return 0
    temp = head
    numNodes = 0
    while temp:
        numNodes += 1
        temp = temp.next
    return numNodes        

def reorderList(head):
    if not head == None and not head.next == None and not head.next.next == None:
        numNodes = getNumNodes(head)
        if numNodes % 2 == 0:
            firstHalf = []
            secondHalf = []
            tempPtr = head
            for i in range(numNodes//2):
                firstHalf.append(tempPtr)
                tempPtr = tempPtr.next
            for i in range(numNodes//2):
                secondHalf.append(tempPtr)
                tempPtr = tempPtr.next
            reverse(secondHalf)
            for i in range(numNodes//2):
                firstHalf[i].next = secondHalf[i]
            for i in range(numNodes//2 - 1):
                secondHalf[i].next = firstHalf[i+1]
        else:
            firstHalf = []
            secondHalf = []
            tempPtr = head
            for i in range(numNodes//2):
                firstHalf.append(tempPtr)
                tempPtr = tempPtr.next
            for i in range(numNodes//2, numNodes):
                secondHalf.append(tempPtr)
                tempPtr = tempPtr.next
            reverse(secondHalf)
            for i in range(numNodes//2):
                firstHalf[i].next = secondHalf[i]
            for i in range(numNodes//2 - 1):
                secondHalf[i].next = firstHalf[i+1] 
