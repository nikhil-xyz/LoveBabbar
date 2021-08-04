t = int(input())
for j in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    ma = arr[0]
    mi = arr[0]
    result = arr[0]

    for i in range(1, n):
        if arr[i] < 0:
            temp = mi
            mi = ma
            ma = temp

        ma = max(arr[i], arr[i] * ma)
        mi = min(arr[i], arr[i] * mi)
        if ma > result:
            result = ma
    print(result)