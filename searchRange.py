def binSearch(nums, target):
    l = 0
    r = len(nums)-1
    while l <= r:
        mid = (l+r)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return -1
    
def searchRange(nums, target):
    ind = binSearch(nums, target)
    if ind == -1:
        return [-1, -1]
    lind = ind
    rind = ind
    while lind >= 0:
        if nums[lind] == target:
            lind -= 1
        else:
            break
    while rind < len(nums):
        if nums[rind] == target:
            rind += 1
        else:
            break
    return [lind+1, rind-1]        
