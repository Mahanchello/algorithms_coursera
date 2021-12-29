def selection_sort(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr       

if __name__ == '__main__':
    arr = [8, 2, 5, 3]
    assert selection_sort2(arr) == [2, 3, 5, 8]
    assert selection_sort(arr) == [2, 3, 5, 8]

#1. given arrya [8, 2, 5, 3]
#2. get array [2, 3, 5, 8]
#3. compare elem with the first elem
#4. if the elem is less -> swap 
#5. continue comparing until the arrya sorted 