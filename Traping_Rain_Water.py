t = int(input())
for tt in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    left = []
    right = []
    left_max = arr[0]
    right_max = arr[n-1]
    for i in range(1, n-1):
        left_max = max(left_max, arr[i])
        right_max = max(right_max, arr[n-i-1])
        left.append(left_max)
        right.append(right_max)
    right.reverse()

    # print(left)
    # print(right)
    result = 0
    for i in range(n-2):
        temp = min(left[i], right[i])
        if arr[i+1] < temp:
            result += (temp - arr[i+1])
    print(result)