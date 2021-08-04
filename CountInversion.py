def merge(arr, l, mid, r):
    inversion = 0
    n1 = mid - l + 1
    n2 = r - mid
    temp1, temp2 = [], []

    for i in range(n1):
        temp1.append(arr[l+i])

    for i in range(n2):
        temp2.append(arr[mid+i+1])

    i, j, k = 0, 0, l
    while (i < n1) & (j < n2):
        if temp1[i] <= temp2[j]:
            arr[k] = temp1[i]
            i += 1
            k += 1
        else:
            arr[k] = temp2[j]
            inversion += n1 - i
            k += 1
            j += 1

    while i < n1:
        arr[k] = temp1[i]
        k += 1
        i += 1

    while j < n2:
        arr[k] = temp2[j]
        k += 1
        j += 1

    return inversion

def mergeSort(arr, l, r):
    inversions = 0
    if l < r:
        mid = int((l + r) / 2)
        inversions += mergeSort(arr, l, mid)
        inversions += mergeSort(arr, mid+1, r)
        inversions += merge(arr, l, mid, r)
    return inversions

n = int(input())
arr = list(map(int, input().split()))

result = mergeSort(arr, 0, n-1)
print(result)