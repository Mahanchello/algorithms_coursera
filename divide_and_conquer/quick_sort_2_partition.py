# sort an array [4, 3, 2, 1] using quick sort 
# in this problem we are using divide and conquer strategy 
# Note: we are using here 2 array partitioning, which is valid only when all the numbers are unique.
# if the numbers are not unique, we need to use 3 array partitioning.
# just because when we partition and numbers are equal, it's incorrect to put them to the left or to the right of the pivot if the pivot is the same. 
# we will end up with quatratic running time. 

def swap(arr, index1, index2):
    arr[index1], arr[index2] = arr[index2], arr[index1]

# 2 array partitioning 
def partition(arr, start, end):
    q = start
    print(end, 'end')
    for j in range(start, end):
        print(j, 'j')
        if arr[j] <= arr[end]:
            swap(arr, j, q)
            q += 1    
    swap(arr, end, q) 
    print(arr, 'arr')
    print(q, 'q')  
    return q

def merge_sort(arr, start, end, indicator=None):
    if indicator:
       print(indicator, 'indicator')
    print(start, 'start before')
    print(end, 'end')
    if start < end:
        print(end, 'end!')
        pivot = partition(arr, start, end)
        merge_sort(arr, start, pivot-1, '1 recursion')
        merge_sort(arr, pivot+1, end, '2 recursion')
    else:
        print("Won't address")    

arr = [4, 3, 2, 1]

merge_sort(arr, 0, len(arr) - 1)
print(arr, 'arr')


# if __name__ == '__main__':
#     arr = [4, 3, 2, 1]
#     merge_sort(arr, 0, len(arr) - 1)
   
