from collections import Counter
t = int(input())
for tt in range(t):
    n = int(input())
    a1 = list(map(int, input().split()))

    arr = list(Counter(a1).items())
    arr = list(sorted(arr, key=lambda x: x[1]))

    size = len(arr)
    if arr[size - 1][1] > int(n / 2):
        print(arr[size - 1][0])
    else:
        print(-1)