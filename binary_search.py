def doSearch(elem_array, target, expected):
    min = 0
    max = len(elem_array) - 1

    while min <= max:
        guess = (min + max) / 2
        if elem_array[guess] == target:
            assert guess == expected
            return 
        elif elem_array[guess] < target:
             min = guess + 1
        else: 
            max = guess - 1
    print('not in the range!')   
    return - 1         


if __name__ == '__main__':
    arr = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]  
    target = 37
    expected = 11

    doSearch(arr, target, expected)