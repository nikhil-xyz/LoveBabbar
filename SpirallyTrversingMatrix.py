t = int(input())
for tt in range(t):
    r, c = map(int, input().split())
    matrix = []
    for i in range(r):
        temp = list(map(int, input().split()))
        matrix.append(temp)
    temp_row, temp_col = 0, 0
    z = 0
    while (z < int(r / 2)) & (z < int(c / 2)):
        x, y = z, z
        while (y < (c - z)) & (x == z):
            print(matrix[x][y], end=" ")
            y += 1
        y -= 1
        x += 1
        while (x < (r - z)) & (y == c - 1 - z):
            print(matrix[x][y], end=" ")
            x += 1
        x -= 1
        y -= 1
        while (y >= z) & (x == r - 1 - z):
            print(matrix[x][y], end=" ")
            y -= 1
        y += 1
        x -= 1
        while (x > z) & (y == z):
            print(matrix[x][y], end=" ")
            x -= 1
        z += 1
    if (abs(r - c) == 1) & ((min(r, c) % 2) == 0):
        continue

    temp = z
    if r > c:
        while temp < (r - z):
            print(matrix[temp][z], end=" ")
            temp += 1
    else:
        while temp < (c - z):
            print(matrix[z][temp], end=" ")
            temp += 1
