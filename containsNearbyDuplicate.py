def containsNearbyDuplicate(nums, k):
    ind = {}
    for i in range(len(nums)):
        if nums[i] in ind:
            ind[nums[i]].append(i)
        else:
            ind[nums[i]] = [i]
    for num,indices in ind.items():
        if len(indices) > 1:
            for i in range(1, len(indices)):
                if indices[i] - indices[i-1] <= k:
                    return True
    return False
