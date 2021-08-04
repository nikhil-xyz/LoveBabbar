t = int(input())
for tt in range(t):
    r, c = map(int, input().split())
    arr = []
    for i in range(r):
        temp = list(map(int, input().split()))
        arr.append(temp)

    result = 0
    for i in range(r):
        for j in range(c):
            if i > 0:
                if arr[i][j] != 0:
                    arr[i][j] += arr[i-1][j]

        temp_min = 100000000
        index = 0
        for j in range(c):
            if arr[i][j] != 0:
                temp_min = min(temp_min, arr[i][j])
            else:
                if j != 0:
                    result = max(result, (j-index) * temp_min)
                index = j + 1
                temp_min = 100000000
    print(result)