# find minimum number in the array [6, 4, 8, 90, 12, 56, 7, 1, 63]
def find_min_number(arr, ind, len):
    # set default minimum 
    minimum = 0
    # base case will be to go through the whole array till the second-to-last index
    if ind >= len - 2:
        # compare second-to-last elem with the last elem 
        if arr[ind] < arr[ind+1]:
            return arr[ind]
        else:
            return arr[ind+1]

    # divide step, recursion call 
    minimum = find_min_number(arr, ind+1, len)
    
    # merge step 
    # as soon as recusrion met base case, it goes forward to the first case through the whole array to the beginning 
    if arr[ind] < minimum:
        return arr[ind]
    else: 
        return minimum    




arr = [6, 4, 8, 90, 12, 56, 7, 1, 63]
print(find_min_number(arr, 0, 9))
# expected output 90