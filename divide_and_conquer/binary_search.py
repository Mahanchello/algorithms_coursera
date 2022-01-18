# Given two arrays, first elem of each array is the length of array. Return index of the elem in arr2 that exists in arr1. If no match, return -1
# arr1 = [5, 1, 5, 8, 12, 13]
# arr2 = [5, 8, 1, 23, 1, 11]
# the goal is to implement binary search algo using devide and conquer strategy

def binary_search(arr, key):
    # define min and max index of the array, we will need them for comparison with the key
    min = 0
    max = len(arr) - 1
    # base case when we min and max elem are the same, that means our array consists of one elem
    if arr[min] == arr[max]:
        # check if min or max index matches with the given key
        if arr[min] == key:
            return min
        else: 
            return -1     

    else:
        # in binary search we need to divide by two an array 
        mid = (min + max) // 2
        # if key is less, search in the left part of the array 
        if key < arr[mid]:
            return binary_search(arr[:mid-1], key)  
        # if key matches, just return mid index         
        elif key == arr[mid]:
            return mid  
        # if key is more, search in the right part of the array      
        else:
            return binary_search(arr[mid+1:], key)                                  




if __name__ == '__main__':
    arr = [5, 1, 5, 8, 12, 13]
    elem = [5, 8, 1, 23, 1, 11]
    res = []
    for i in range(1, len(elem)):
        res.append(binary_search(arr[1:], elem[i]))
    print(res, 'res')    

    # expected res: [2, 0, -1, 0, -1]   