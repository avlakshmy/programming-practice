def filterRestaurants(restaurants, veganFriendly, maxPrice, maxDistance):
    ans = []
    for res in restaurants:
        if veganFriendly and res[2] == False:
            continue
        if res[3] > maxPrice:
            continue
        if res[4] > maxDistance:
            continue
        ans.append(res)
    ans.sort(key=lambda x:(x[1], x[0]))
    ans = ans[::-1]
    return [a[0] for a in ans]
