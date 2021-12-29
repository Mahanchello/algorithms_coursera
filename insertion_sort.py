# sort array [22, 11, 99, 88, 9, 7, 42] using insertion sort 

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j + 1] = key 
    return arr           


if __name__ == '__main__':
    arr = [22, 11, 99, 88, 9, 7, 42]
    print(insertion2(arr))
    assert insertion_sort(arr) == [7, 9, 11, 22, 42, 88, 99]     

