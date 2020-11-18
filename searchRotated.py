def search(nums, target):
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = (low + high)//2
        if target == nums[mid]:
            return mid
        elif target < nums[mid]:
            if target < nums[0] and nums[mid] >= nums[0]:
                low = mid+1
            else:
                high = mid-1
        else:
            if target > nums[-1] and nums[mid] <= nums[-1]:
                high = mid-1
            else:
                low = mid+1                   
    return -1
