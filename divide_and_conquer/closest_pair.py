import math 

def get_distance(x1, y1, x2, y2):
    print(x1, y1, x2, y2, 'x1, y1, x2, y2')
    return math.sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2))

# naive solution
def naive_solution(x, y):
    min_distance = float('inf')
    for i in range(len(x)-1):
        for j in range(i+1, len(y)):
            distance = get_distance(x[i], y[i], x[j], y[j])
            print(distance, 'distance')
            if distance < min_distance:
                min_distance = distance
    return min_distance 

# same naive solution, but when sorted array is passed
def brute_force(sorted_array):
    min_distance = float('inf')
    for i in range(len(sorted_array)-1):
        for j in range(i+1, len(sorted_array)):
            distance = get_distance(sorted_array[i][0], sorted_array[i][1], sorted_array[j][0], sorted_array[j][1])
            if distance < min_distance:
                min_distance = distance
    return min_distance    

def find_min(sorted_arr, min_d):
    # get middle line 
    mid = len(sorted_arr) // 2
    mid_value = sorted_arr[mid][0]
    # intialize sorted by y-coordinate array 
    sorted_y_array = []
    # filter the initial point set and keep only those points whose x-distance to the middle line does not exceed d
    for point in sorted_arr:
        if abs(point[0] - mid_value) < min_d:
            sorted_y_array.append(point)  
    # sort set of points by y-coordinate        
    sorted_y_array.sort(key = lambda x: x[1])     
    len_strip = len(sorted_y_array)
    if len_strip < 2:
        return min_d
    else:
        # compute each point distance to the seven subsequent points and compute the min distance
        min_d2 = get_distance(sorted_y_array[0][0], sorted_y_array[0][0], sorted_y_array[1][0], sorted_y_array[1][1])    
        for i in range(len_strip-1):
            for j in range(i+1, min(i + 7, len_strip)):
                min_d2 = min(min_d2, get_distance(sorted_y_array[i][0], sorted_y_array[i][1], sorted_y_array[j][0], sorted_y_array[j][1]))
        return min_d2        
    

# have a sorted array as an argument
def fast_solution(sorted_arr):
    # base case
    if len(sorted_arr) <= 3:
        # calculate distance using naive approach
        return brute_force(sorted_arr)
    # split array     
    mid = len(sorted_arr) // 2
    # solve problem for each splitted array recursively
    d1 = fast_solution(sorted_arr[:mid])
    d2 = fast_solution(sorted_arr[mid:])
    # get min distance from both results
    d = min(d1, d2)
    min_d = find_min(sorted_arr, d)
    result = min(d, min_d)
    return result


    


if __name__ == '__main__':
    # x = [0, 3]
    # y = [0, 4]
    # x = [4, -2, -3, -1, 2, -4, 1, -1, 3, -4, -2]
    # y = [4, -2, -4, 3, 3, 0, 1, -1, -1, 2, 4]
    x = [0, 5, 3, 7]
    y = [0, 6, 4, 2]
    # first we need to sort input by x coordinate
    sorted_array = []
    for i in range(len(x)):
        sorted_array.append((x[i], y[i]))  
    sorted_array.sort()
    print(fast_solution(sorted_array))

