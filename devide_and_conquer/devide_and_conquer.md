## Devide and Conquer algorithm 

1. Break into non-overlapping subproblems of the same type 
2. Recursevily solve those subproblems 
3. Combine results 


Linear search recursive solution: 
```
LinearSearch(A, low, igh, key):
if high < low:
    return NOT_FOUND
if A[low] = key:
    return low 
return LinerSearch(A, low + 1, high, key)
```
(this is not a solution that would fit devide and conquer algorithm :pointupindex:)



