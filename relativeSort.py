def relativeSortArray(arr1, arr2):
    freq = {}
    others = []
    for num in arr1:
        if num in arr2:
            freq[num] = arr1.count(num)
        else:
            others.append(num)
    others.sort()
    ans = []
    for num in arr2:
        ans.extend([num for _ in range(freq[num])])
    ans.extend(others)
    return ans
