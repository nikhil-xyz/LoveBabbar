n, x = map(int, input().split())
arr = list(map(int, input().split()))

prefix = [arr[0]]
for i in range(1, n):
    prefix.append(arr[i] + prefix[i-1])

result = n
i, j = 0, 0
while i < n:
    if prefix[i] > x:
        while (prefix[i] - prefix[j]) > x:
            j += 1
        temp = i - j + 1
        result = min(result, temp)
    i += 1
print(result)



