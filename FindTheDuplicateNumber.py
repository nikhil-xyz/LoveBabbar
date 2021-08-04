from collections import Counter
string = input()
string = string[1:len(string)-1]
arr = list(map(int, string.split(",")))
freq = Counter(arr)
for i in freq.keys():
    if freq[i] > 1:
        print(i)
        break
