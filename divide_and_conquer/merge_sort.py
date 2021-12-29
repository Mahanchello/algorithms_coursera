def merge_sort(arr):
    # base case 
    if len(arr) <= 1:
        return arr 
    
    # divide list into 2 parts 
    mid_arr = len(arr) // 2
    # run recursion on each part
    left = merge_sort(arr[:mid_arr])
    right = merge_sort(arr[mid_arr:])
    # merge two partitions
    return merge(arr, left, right)

def merge(arr, left, right):
    output = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            output.append(left[i])
            i += 1
        else:
            output.append(right[j])
            j += 1 

    output.extend(left[i:])  
    output.extend(right[j:])  
    return output         


print(merge_sort([4, 3, 2, 1]))

