t = int(input())
for i in range(t):
    n = int(input())

    arr = [1]
    for j in range(2, n+1):
        remain = 0
        for k in range(len(arr)-1, -1, -1):
            temp = arr[k]
            arr[k] = ((temp * j) + remain) % 10
            remain = int(((temp * j) + remain) / 10)

        while remain != 0:
            temp = remain
            arr.insert(0, remain % 10)
            remain = int(remain / 10)

    print(arr)
