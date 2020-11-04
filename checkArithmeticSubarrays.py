def canMakeArithmeticProgression(arr):
    arr.sort()
    diff = arr[1] - arr[0]
    for i in range(2, len(arr)):
        if not arr[i] - arr[i-1] == diff:
            return False
    return True
        
def checkArithmeticSubarrays(nums, left, right):
    ans = []
    for l,r in zip(left,right):
        sub = nums[l:r+1]
        ans.append(canMakeArithmeticProgression(sub))
    return ans
        
