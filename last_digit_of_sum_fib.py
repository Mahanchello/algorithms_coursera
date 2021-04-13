# Last Digit of the Sum of Fibonacci Numbers
# Task.Given an integer n, find the last digit of the sum F0 + F1 + ... + Fn.

# Sample 1        # Sample 2
# Input:          # Input:
# 3               # 100
# Output:         # Output:
# 4               # 5


mod = 10
def getPisano():
 current, previous = 1, 0
 for i in range(mod * mod):
  previous, current = current, (previous + current) % mod
  if(previous == 0 and current == 1):
   return i + 1

def fibSum(n):
 current, previous = 1, 0
 res = 1
 pis = getPisano()
 n = n % pis 
 if n == 0:
  return 0
 elif n == 1:
  return 1
  
 for i in range(n - 1):
  previous, current = current, previous + current
  res += current
 
 return res % mod

print(fibSum(100)) 