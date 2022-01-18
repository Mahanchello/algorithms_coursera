# naive algorithm, wher running time is quadratic
def naive_count_segments(starts, ends, points):
    res = []
    count = 0
    for j in points:
        for i in range(len(starts)):
            if j <= ends[i] and j >= starts[i]:
                count += 1
        res.append(count)
        count = 0
    return res                  

def fast_count_segments(starts, ends, points):
    # create an empty array where we will store starts, ends and points with indicators
    main_array = []
    # append to the array starts, ends and points with indicators
    for i in range(len(starts)):
        main_array.append((starts[i], 's')) # s means start 
        main_array.append((ends[i], 'e')) # e means end 
    for point in points:
        main_array.append((point, 'p')) # p means point

    # sort an array 
    main_array.sort()
    

    res = {}
    segment_count = 0
    # loop through the main_array and count segments 
    for i in range(len(main_array)):
        # if elem has 's' means start, count segment 
        if main_array[i][1] == 's':
            segment_count += 1
        # if elem has 'e' means end, substract 1 segment    
        elif main_array[i][1] == 'e':
             segment_count -= 1
        # assign segment count to the point     
        else: 
            res[main_array[i][0]] = segment_count 
    res1 = []        
    for point in points:
        res1.append(res[point])  
    return res1           


print(fast_count_segments([0, -3, 7], [5, 2, 10], [1, 6]))
