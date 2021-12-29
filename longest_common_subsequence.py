def lcs(a, b):
    # create a matrix and set first row and each firat column to be 0
    T = [[float('inf') for i in range(len(b) + 1)] for j in range(len(a) + 1)]
    for i in range(len(a) + 1):
        T[i][0] = 0
    for j in range(len(b) + 1):
        T[0][j] = 0
 

    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i-1] == b[j-1]:
                T[i][j] = T[i-1][j-1] + 1
            else:
                T[i][j] = max(T[i-1][j], T[i][j-1])

    return T[len(a)][len(b)]
        

print(lcs([1, 2, 3], [3, 2, 1]))

     