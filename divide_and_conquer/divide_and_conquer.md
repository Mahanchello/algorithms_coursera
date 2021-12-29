## Devide and Conquer algorithm 

1. Break into non-overlapping subproblems of the same type 
2. Recursevily solve those subproblems 
3. Combine results 


Linear search recursive solution: 
```
LinearSearch(A, low, high, key):
if high < low:
    return NOT_FOUND
if A[low] = key:
    return low 
return LinerSearch(A, low + 1, high, key)
```
(this is not a solution :point_up_2: that would fit trivial definition of divide and conquer algorithm,
because the probmlem is not split into subproblem)

A **recurrence relation** is an equation recursevily defining a sequence of values. 

When we're doing runtime analysis for divide and conquer algorithms,
we usually define a **recurrence relation** for t event,
where t stands for the worst case time taken or the algorithm,
and n is the size of the problem. 
(Example: for linear search worst case scenario will be when the elem is not found).


```
BinarySearch(A, low, high, key):
if high < low:
    return low - 1
mid = low + (high-low)/2
if key = A[mid]:
    return mid
else if key < A[mid]:
    return BinarySearch(A, low, mid - 1, key)
else if key > A[mid]:
    return BinarySearch(A, low, mid + 1, key)
```

Summary: 
- break problem into non-overlapping subproblems of the same type 
- recursively solve those subproblems 
- combine results of subproblem 

Runtime: O(log n)









