# Least Common Multiple
# Task.Given two integers a and b, find their least common multiple.


# Sample 1          # Sample 2
# Input:            # Input:
# 6 8               # 28851538 1183019
# Output:           # Output:
# 24                # 1933053046


def EuclidGcd(a, b):
 if b == 0:
  return a
 a_prime = a % b
 return EuclidGcd(b, a_prime)

def fastAlgo(a, b):
    lcm = (a*b) // EuclidGcd(a, b)
    return lcm


print(fastAlgo(28851538, 1183019))