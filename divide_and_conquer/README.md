## Divide and Conquer strategy 

![Divide and conquer algo schema](divide_and_conquer.png)

1. **Break** into non-overlapping subproblems of the same type 
2. **Recursevily** solve those subproblems 
3. **Combine** results 

*One important thing is whatever the main problem is the sub-problem will be the same as main problem!* (example if the main problem is to sort, the subproblem should be sort as well)

Linear search recursive solution: 
```
LinearSearch(A, low, high, key):
if high < low:
    return NOT_FOUND
if A[low] = key:
    return low 
return LinerSearch(A, low + 1, high, key)
```

A **recurrence relation** is an equation recursevily defining a sequence of values. 

When we're doing runtime analysis for divide and conquer algorithms,
we usually define a **recurrence relation** for t event,
where t stands for the worst case time taken for the algorithm,
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
for the binary search problem above :point_up_2: we are using Decrease and Conquer strategy. (because there is only one sub-problem and no merge step)

Summary: 
- **break** problem into non-overlapping subproblems of the same type 
- **recursively solve** those subproblems 
- **combine** results of subproblem 

There are some sorting algorithms that follow divide and conquer strategy: 
- Quick sort 
- Merge Sort
- Finding maximum and mimimum
- Linear search
- Binary Search 
- Closest pair of Points 
- Strassen's algorithm 
- Karatsuba algorithm for fast multiplication 

Runtime: O(n log n)









