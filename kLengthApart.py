def kLengthApart(nums, k):
    indices = []
    for i in range(len(nums)):
        if nums[i] == 1:
            indices.append(i)
    for i in range(len(indices) - 1):
        if indices[i+1] - indices[i] <= k:
            return False
    return True
