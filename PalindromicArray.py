t = int(input())
for tt in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    flag = True
    for i in range(n):
        string = str(arr[i])
        j, k = 0, len(string) - 1
        while j < k:
            if string[j] != string[k]:
                flag = False
                break
            j += 1
            k -= 1
        if flag is not True:
            break
    if flag is not True:
        print(0)
    else:
        print(1)