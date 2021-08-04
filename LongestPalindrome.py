t = int(input())
for tt in range(t):
    string = input()
    result_length = 1
    result_string = string[0]

    matrix = []
    for i in range(len(string)):
        temp = []
        for j in range(len(string)):
            if i == j:
                temp.append(1)
            else:
                temp.append(0)
        matrix.append(temp)

    for i in range(1, len(string)):
        for j in range(len(string)-i):
            if string[j] == string[i+j]:
                if i == 1:
                    matrix[j][j+i] = 1
                    if (i+1) > result_length:
                        result_length = i+1
                        result_string = string[j:j+i+1]
                        continue
                if matrix[j+1][j+i-1] == 1:
                    matrix[j][j+i] = 1
                    if (i + 1) > result_length:
                        result_length = i+1
                        result_string = string[j:j + i + 1]

    print(result_string)