from bisect import bisect_right
t = int(input())
for tt in range(t):
    size, n = map(int, input().split())
    arr = list(map(int, input().split()))

    arr.sort()
    flag = False
    for i in arr:
        index = bisect_right(arr, n + i)
        if (arr[index - 1] - i) == n:
            print(1)
            flag = True
    if flag is not True:
        print(-1)