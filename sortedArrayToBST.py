def sortedArrayToBST(nums):
    if len(nums) == 0:
        return None
    mid = len(nums)//2
    root = TreeNode(nums[mid])
    root.left = sortedArrayToBST(nums[:mid])
    root.right = sortedArrayToBST(nums[mid+1:])
    return root
