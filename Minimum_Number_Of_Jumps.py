n = int(input())
arr = list(map(int, input().split()))

i = 0
steps = 0
while i < n:
    current_stair = i + 1
    best_ladder = n
    for j in range(current_stair, current_stair + arr[i]):
        if (n - (j + arr[j])) < best_ladder:
            best_ladder = n - (j + arr[j])
            i = j
        if j == n - 1:
            i = n
            break
    steps += 1
    if best_ladder == n:
        steps = -1
        break
print(steps)


