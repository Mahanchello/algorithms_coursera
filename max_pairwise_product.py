# Maximum Pairwise Product Problem
# Find the maximum product of two distinct numbers 
# in a sequence of non-negative integers.

# Input:A sequence of non-negativeintegers.
# Output:The maximum value thatcan be obtained  
# by multiplyingtwo different elements from the se-quence.

# Sample 1        # Sample 2 
# input:          # input: 
# 3               # 10
# 1 2 3           # 7 5 14 2 8 8 10 1 2 3
# output:         # output: 
# 6               # 140 

#a = [int(x) for x in input().split()]
a = [7, 5, 14, 2, 8, 8, 10, 1, 2, 3]
n = 10
assert(len(a) == n)

arr = a
maxn1 = arr[0]
maxi = 0
for i in range(0, len(arr)):
 if arr[i] > maxn1:
  maxn1 = arr[i]
  maxi = i
  
  
            
maxn2 = 0
for j in range(0, len(arr)):
 if arr[j] > maxn2 and maxi != j:
  maxn2 = arr[j]  
print(maxn1 * maxn2)