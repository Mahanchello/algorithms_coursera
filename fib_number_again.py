# Fibonacci Number Again
#Task.Given two integers n and m, output c mod m(that is, the remainder of c when divided by m).


# Sample 1        # Sample 2
# Input:          # Input: 
# 239 1000        # 2816213588 239 
# Output:         # Output
# 161             # 151


#get pisano period
def getPisanoPer(m):
 current, previous = 1, 0
 # loop through the m in the power of m 
 for i in range (m * m):
  previous, current = current, (previous + current) % m
  # when we see that the previos and current is equal to our intial value, that means the pisano period will be starting again, hence we should exit the loop 
  if(previous == 0 and current == 1):
   # we have to add + 1 to get exact length of the pisanoPeriod 
   return i + 1
  
def getFibHuge(n, m):
 current, previous = 1, 0
 # get pisano period
 pis = getPisanoPer(m)
 # get mod of the index of fib number, because we know every nth index of fib number has the same mode according to the pisano period
 n = n % pis
 
 if n == 0:
  return 0
 elif n == 1:
  return 1
 
 # loop through the remainder (we do n -1, because we need to loop through the length, for example 7 elements have length of 6, because we start counting from 0)
 for i in range(n-1):
  #basically we compute fib from the mod  
  previous, current = current, current + previous
 # found the mod from the current number
 return current % m

print(getFibHuge(2816213588, 239))