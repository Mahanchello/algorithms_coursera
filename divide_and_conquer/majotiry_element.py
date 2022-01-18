# check if the array contains majority elem. If it does -> return 1, if not -> return 0.
# Majority elem is the elem with the occurence in the array more then n/2 
# example: in array [1, 2, 3, 1] -> 1 is not a majority elem, because it's occured in the array n/2 times, should be more than n/2 times.
def majorityElement(arr, lo=0, hi=None):
    def majority_elem(lo, hi, indicator):
        print(lo, 'lo')
        print(hi, 'hi')
        print(indicator, 'indicator')
        # base case when left == right 
        if lo == hi:
            return arr[lo] 
        
        # split on sub-tasks
        mid = (lo + hi) // 2
        print(mid, 'mid')
        left = majority_elem(lo, mid, indicator='left')
        print(left, 'left')
        print(mid+1, 'mid+1')
        print(hi, 'hi')
        right = majority_elem(mid+1, hi, indicator='right')
        print(right, 'right')
        
        if left == right:
            return left 
        print(lo, 'lo')
        print(hi+1, 'hi+1')
        left_count = sum(1 for i in range(lo, hi+1) if arr[i] == left)
        print(left_count, 'left_count')
        right_count = sum(1 for i in range(lo, hi+1) if arr[i] == right)
        print(right_count, 'right_count')     


        return left if left_count > right_count else right
    print('got here!!!!!!')    
    return majority_elem(0, len(arr)-1, indicator=None)   

arr = [2, 3, 9, 2, 2]
print(majorityElement(arr, 0))



# def majority_elem(arr, lo, hi):

