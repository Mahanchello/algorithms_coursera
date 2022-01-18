def lcs3(a, b, c):
    matrix = [[[float('-inf') for i in range(len(a) + 1)] for y in range(len(b) + 1)] for x in range(len(c)+1)]
    for i in range(len(c)+1):
        for j in range(len(b)+ 1):
            for z in range(len(a) + 1):
                if i == 0 or j == 0 or z == 0:
                    matrix[i][j][z] = 0

    for i in range(1, len(c) + 1):
        for j in range(1, len(b) + 1):
            for z in range(1, len(a) + 1):
                if c[i-1] == b[j-1] and c[i-1] == a[z-1]:
                    matrix[i][j][z] = matrix[i-1][j-1][z-1] +1
                else: 
                    matrix[i][j][z] = max(matrix[i-1][j][z], matrix[i][j-1][z], matrix[i][j][z-1], matrix[i-1][j-1][z], matrix[i-1][j][z-1], matrix[i][j-1][z-1])     
    return matrix[len(c)][len(b)][len(a)]                    


print(lcs3([8, 3, 2, 1, 7], [8, 2, 1, 3, 8, 10, 7], [6, 8, 3, 1, 4, 7])) # expected 3