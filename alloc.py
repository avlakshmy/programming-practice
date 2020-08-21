T = int(input())
for i in range(T):
    nb = [int(x) for x in input().split()]
    N = nb[0]
    B = nb[1]
    A = [int(x) for x in input().split()]
    A.sort()
    if len(A) > 1:
        cost = 0
        j = 0
        while j < len(A):
            cost += A[j]
            if cost > B:
                break
            j += 1
        print('Case #{}: {}'.format(i+1, j))
    else:
        if A[0] <= B:
            print('Case #{}: 1'.format(i+1))
        else:
            print('Case #{}: 0'.format(i+1))
