t = int(input())
for tt in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    sum1 = 0
    for i in range(0, n, 2):
        sum1 += arr[i]

    sum2 = 0
    for i in range(1, n, 2):
        sum2 += arr[i]

    print(max(sum1, sum2))