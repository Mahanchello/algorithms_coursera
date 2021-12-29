# This is an example of the dynamic programming challenge

def amount_gold(W, n):
    # frist create synamic programming matrix
    T = [[float('inf') for i in range(len(n)+1)] for j in range(W+1)]
    # set each first column to be zero 
    for i in range(len(n)+1):
        T[0][i] = 0
    # set each first row to be zero     
    for j in range(W+1):
        T[j][0] = 0
    
    # let's loop through the total weight 
    for i in range(1, W+1):
        # let's loop through the weight of each elem
        for j in range(1, len(n)+1):
            # set each elem in matrix to be what's the above 
            T[i][j] = T[i][j-1]
            # then if the current elem weight does not exceed the current weight from the total amount
            if n[j-1] <= i:
                # use below formula to get the value
                val = T[i-n[j-1]][j-1] + n[j-1]
                if T[i][j] < val:
                    T[i][j] = val               
    return T[W][len(n)]                




amount_gold(10, [1, 4, 8])