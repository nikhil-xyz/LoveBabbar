from collections import Counter
t = int(input())
for i in range(t):
    n, x = map(int, input().split())
    arr = list(map(int, input().split()))

    frequency = Counter(arr)
    arr = list(sorted(set(arr)))

    count = 0
    for j in range(len(arr)-2):
        remain = x - arr[j]
        temp1 = frequency[arr[j]]

        k = j + 1
        l = len(arr) - 1
        while arr[k] < int(remain / 2):
            while arr[l] > (remain - arr[k]):
                l -= 1
            if arr[l] == (remain - arr[k]):
                temp2 = frequency[arr[k]]
                temp3 = frequency[arr[l]]
                count += temp1 * temp2 * temp3
            k += 1
    print(count)


