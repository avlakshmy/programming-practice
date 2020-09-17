def zigZag(arr, n):
	for i in range(n-1):
	    if i%2 == 0:
	        if arr[i] > arr[i+1]:
	            arr[i], arr[i+1] = arr[i+1], arr[i]
	    else:
	        if arr[i] < arr[i+1]:
	            arr[i], arr[i+1] = arr[i+1], arr[i]

tc = int(input())
while tc > 0:
    n = int(input())
    arr = list(map(int, input().strip().split()))
    zigZag(arr, n)
    for x in arr:
        print(x, end=" ")
    print()
    tc -= 1
