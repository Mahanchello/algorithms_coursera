# Greatest Common Divisor
# Task. Given two integers a and b, find their greatest common divisor.

# Sample 1        # Sample 2
# Input:          # Input:
# 18 35           # 28851538 1183019
# Output:         # Output:
# 1               # 17657 

def EuclidGcd(a, b):
 if b == 0:
  return a
 a_prime = a % b
 return EuclidGcd(b, a_prime)

print(EuclidGcd(28851538, 1183019))

