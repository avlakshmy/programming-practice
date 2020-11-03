def distributeCandies(candies, num_people):
    dist = [0 for _ in range(num_people)]
    curr = 1
    i = 0
    while curr <= candies:
        dist[i] += curr
        candies -= curr
        curr += 1
        i = (i+1)%num_people
    if candies > 0:
        dist[i] += candies
    return dist
        
