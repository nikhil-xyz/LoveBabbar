arr = list(map(int, input().split()))
index1, index2 = -1, 0
for i in range(len(arr) - 2, -1, -1):
    if arr[i] < arr[i + 1]:
        index1 = i
        break

if index1 > -1:
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] > arr[index1]:
            index2 = i
            break
    temp = arr[index1]
    arr[index1] = arr[index2]
    arr[index2] = temp

diff = int((len(arr) - (index1 + 1)) / 2)
for i in range(index1 + 1, index1 + 1 + diff):
    temp = arr[i]
    arr[i] = arr[len(arr)-(i-index1)]
    arr[len(arr)-(i-index1)] = temp
print(arr)
