def inorderTraversal(root):
    if root == None:
        return []
    ans = []
    if not root.left == None:
        ans.extend(inorderTraversal(root.left))
    ans.append(root)
    if not root.right == None:
        ans.extend(inorderTraversal(root.right))
    return ans
        
def binarySearch(arr, val):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid].val == val:
            return True
        elif arr[mid].val < val:
            low = mid+1
        else: # arr[mid] > val
            high = mid-1
    return False
    
def findTarget(root, k):
    arr = inorderTraversal(root)
    for node in arr:
        if not (node.val == k - node.val) and binarySearch(arr, k-node.val) == True:
            return True
    return False
