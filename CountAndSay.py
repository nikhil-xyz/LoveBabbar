n = int(input())
result = "1"
i = 2
while i <= n:
    hold = ""
    if len(result) == 1:
        result = "11"
        i += 1
        continue
    temp = 1
    j = 1
    while j < len(result):
        if result[j] == result[j-1]:
            temp += 1
        else:
            hold += str(temp)
            hold += str(result[j-1])
            temp = 1
        j += 1
    hold += str(temp)
    hold += str(result[j - 1])
    result = hold
    i += 1
print(result)