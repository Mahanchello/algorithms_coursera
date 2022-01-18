""" Problem: quick sort array arr = [2, 3, 9, 2, 2] that has duplicated numbers.
Here we are using divide and conquer approach, the only thing since we have non-unique elems in the list, 
we need to use 3 parts array partitioning.
Such implementation has logarithmic running time.
"""

# 3 partitioning array, where array will be split into 3 parts
# first part is less than pivot
# second part is equal to pivot 
# third part is more than the pivot 
def partition3(arr, l, r):
    # assign pivot, start and and the end of the middle parition, where elems are equal to the pivot
    pivot = l
    start = pivot 
    end = pivot
    for i in range(1, r):
        if arr[i] < arr[pivot]:
            # change pivot with the elem if it's less than the pivot 
            arr[i], arr[pivot] = arr[pivot], arr[i]
            # assign pivot to ith, since we swapped elems 
            pivot = i
            # start and end will be equal to pivot 
            start = pivot
            end = pivot 
        elif arr[i] == arr[pivot]:
            # if the elems are equal, we need to increase end of the partitioning 
            end = end + 1
            # change elem with index end with the elem that is equal to pivot
            arr[i], arr[end] = arr[end], arr[i]             
    return start, end    


def quick_sort(arr, l, r):
    if l >= r:
        return
    i, j = partition3(arr, l, r)
    quick_sort(arr, l, i-1)
    quick_sort(arr, j+1, r)


arr = [2, 9, 3, 2, 2]
quick_sort(arr, 0, len(arr))
print(arr, 'arr')
# expected: [2, 2, 2, 3, 9]