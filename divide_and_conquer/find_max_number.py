# given an array [6, 4, 8, 90, 12, 56, 7, 1, 63], find max number in the array;

def divide_and_conquer_max(arr, ind, len):
    # set smaximum 
    maximum = -1 

    # set base case, when the problem is small enough to be solved (conquer step)
    # that's what will be returned from the recursion call later when we meet base case 
    # here we compare index with the second-to-last index in the array, since we are counting from 0, we do len-2
    if ind >= len - 2:
        # compare second-to-last elem with the last elem
        if arr[ind] > arr[ind+1]:
            return arr[ind]
        else: 
            return arr[ind+1]

    # recursion call, that's where we do division on sub-problem
    maximum = divide_and_conquer_max(arr, ind + 1, len)
    # we get maximum that we can combine 

    # combime step 
    # remember as soon as recursion call hit the base case it will go upward to the begging until it will be solved for all the elems
    if maximum > arr[ind]:
        return maximum
    else: 
        return arr[ind]    

 

arr = [6, 4, 8, 90, 12, 56, 7, 1, 63]
print(divide_and_conquer_max(arr, 0, 9))
# expected output 90