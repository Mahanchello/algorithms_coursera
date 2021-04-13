# Fibonacci Number
# Task. Given an integer n, find the nth Fibonacci number.
# Sample 
# input:
# 10
# output: 
# 55 

def calc_fib(n):
    firstNum = 0
    secNumber = 1
    if (n <= 1):
         return n
    for i in range(1, n):
         res = firstNum + secNumber
         firstNum = secNumber
         secNumber = res 
    return res
     

print(calc_fib(10))
