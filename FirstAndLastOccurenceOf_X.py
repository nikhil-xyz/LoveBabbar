t = int(input())
for tt in range(t):
    n, x = map(int, input().split())
    arr = list(map(int, input().split()))

    index1 = 0
    index2 = 0
    flag = False
    for i in range(n):
        if (arr[i] == x) & (flag == False):
            index1 = i
            flag = True
            continue
        if flag & (arr[i] != x):
            index2 = i - 1
            break
    print(index1, index2, sep=" ")