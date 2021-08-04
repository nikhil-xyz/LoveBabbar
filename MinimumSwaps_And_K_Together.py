n = int(input())
arr = list(map(int, input().split()))
k = int(input())

temp = []
present = 0
result = n
total = 0
for i in arr:
    if i > k:
        total += 1

if (total == n) | (total == 0):
    print(0)
for i in range(n):
    temp.append(arr[i])
    if arr[i] > k:
        present += 1
    if i >= (n - total - 1):
        result = min(result, present)
        if arr[i-(n-total-1)] > k:
            present -= 1


print(result)
