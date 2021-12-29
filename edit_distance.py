""" this is a common problem to solve popular Levenshtein distance problem
The Levinstein distance is a similarity measure between words.
Given two words, the distance measures the number of edits needed to transform one word into another. 
There are three techniques that can be used: insertion, deletion, replacement(substitution).
""" 

def edit_distance(s, t):
    # let's create 2d matrix 
    T = [[float('inf') for x in range(len(t)+1)] for y in range(len(s)+1)]
    # fill up first row 
    for i in range(len(s)+1):
        T[i][0] = i
    # fill up first column
    for j in range(len(t)+1): 
        T[0][j] = j     

    for i in range(1, len(s) + 1):
        for j in range(1, len(t) + 1):
            if s[i-1] == t[j-1]:
                diff = 0
            else: 
                diff = 1

            T[i][j] = min(T[i][j-1] + 1, T[i-1][j] + 1, T[i-1][j-1] + diff)                
    return T[len(s)][len(t)] 


print(edit_distance('shorts', 'ports'))

