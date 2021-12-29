def naive_algo_for_lottery(starts, ends, points):
    res = []
    count = 0
    for j in points:
        for i in range(len(starts)):
            if j <= ends[i] and j >= starts[i]:
                count += 1
        res.append(count)
        count = 0
    return res    


def countSegements(starts_left, starts_right, ends_left, ends_rigth, points):
    res = []
    i = 0
    count = 0
    while i < len(points):
        print(points, 'points')
        print(res, 'res1')
        if points[0] >= starts_left[0] and points[0] <= ends_left[0]:
            print('here')
            i += 1
            count += 1
        elif points[0] >= starts_right[0] and points[0] <= ends_rigth[0]:
            i += 1
            count += 1
        else:
            i += 1
    res.append(count)      
    return res, points

def org_lottery_fast(starts, ends, points):
    if len(starts) == 1 and len(ends) == 1:
        return starts, ends 
    midStart = len(starts) // 2
    midEnd = len(ends) // 2
    print(midStart, 'midStart')
    starts_left, ends_left = org_lottery_fast(starts[:midStart], ends[:midEnd], points)
    starts_right, ends_right = org_lottery_fast(starts[midStart:], ends[midEnd:], points) 
    print(starts_left, ends_left, 'starts_left, ends_left')
    print(starts_right, ends_right, 'starts_right, ends_right')
    countSeg, points = countSegements(starts_left, starts_right, ends_left, ends_right, points)
    return countSeg

print(org_lottery_fast([1, -10], [3, 10], [-100, 100, 0]), 'answer')
