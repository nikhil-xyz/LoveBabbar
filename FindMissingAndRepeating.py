t = int(input())
for tt in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()

    missing, repeater = 0, 0
    for i in range(1, n):
        if arr[i] == arr[i-1]:
            repeater = arr[i]
            break
    arr = set(arr)
    i = 1
    for j in arr:
        if i != j:
            missing = i
            break
        i += 1
        if (i == n) & (j == n-1):
            missing = n
    print(repeater, missing)