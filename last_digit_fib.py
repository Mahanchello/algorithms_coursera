# Last Digit of a Large Fibonacci Number
# Task. Given an integer n, find the last digit of the n-th Fibonacci number.

# Sample 1         # Sample 2
# Input:           # Input:
# 331              # 327305 
# Output:          # Output: 
# 9                # 5

def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for i in range(n - 1):
        res = (current + previous) % 10
        previous = current
        current = res
    return res

print(get_fibonacci_last_digit_naive(327305))

