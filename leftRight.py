T = int(input())
for _ in range(T):
    N = int(input())
    arr = [int(x) for x in input().split()]
    currmin = arr[:]
    currmax = arr[:]
    for i in range(1, N):
        if currmax[i] < currmax[i-1]:
            currmax[i] = currmax[i-1]

    for i in range(N-2, -1, -1):
        if currmin[i] > currmin[i+1]:
            currmin[i] = currmin[i+1]

    flag = 0
    for i in range(1, N-1):
        if arr[i] == currmin[i] and arr[i] == currmax[i]:
            flag = 1
            print(arr[i])
            break

    if flag == 0:
        print(-1)
