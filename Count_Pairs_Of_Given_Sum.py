from collections import Counter
n, k = map(int, input().split())
arr = list(map(int, input().split()))

freq = Counter(arr)
keys = list(set(arr))
keys.sort()

result = 0
for i in keys:
    if (i * 2) == k:
        freq1 = freq[i]
        result += int((freq1 * (freq1 - 1)) / 2)
        del freq[i]
        continue

    freq1 = freq[i]
    del freq[i]
    freq2 = freq[k - i]
    del freq[k - i]
    result += (freq1 * freq2)

print(result)
