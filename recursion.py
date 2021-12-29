def factorial(n):
    if n == 0:
        return 1   
    return n * factorial(n - 1)


if __name__ == '__main__':
    assert factorial(5) == 120
    print(factorial_non_recursion(5), 'factorial_non_recursion(5)')
    assert factorial_non_recursion(5) == 120