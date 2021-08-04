n = int(input())
arr = list(map(int, input().split()))
a, b = map(int, input().split())

i = 0
left, right = 0, len(arr)-1

while i < n:
    while arr[left] > b:
        temp = arr[left]
        arr[left] = arr[right]
        arr[right] = temp
        right -= 1

    if left == i:
        i += 1
    while arr[left] > a:
        temp = arr[left]
        arr[left] = arr[i]
        arr[i] = temp
        i += 1

    if arr[left] < a:
        left += 1