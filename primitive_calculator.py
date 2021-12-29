# long method
def primitive_calculator(n):
    min_operations = 0
    res = []
    res.append(n)
    while n > 1:
        if n % 2 == 0:
            min_operations += 1
            n = n / 2
            res.append(n)
        elif n % 3 == 0:
            min_operations += 1
            n = n / 3
            res.append(n)
        else:
            min_operations += 1
            n = n - 1
            res.append(n)
    return min_operations, res[::-1]

# fast method using dynamic (bottom-up) programming approach
def primitive_calculator(n):
    # define an array where we store the number of minimum operations for each interation from [0, 1 to n-1]
    # since we know that to get 0 and 1 we need 0 operations, we set two first elems of the array to 0
    num_operations = [0, 0] + [float('inf')] * (n - 1)
    # then loop through each number in n, starting from 2 
    # (remember, first two elems are 0 and 1, which require 0 operations)
    # we use n + 1 to unclude the number itself on the interation
    for i in range(2, n+1):
        # specify some intermediate values for each operation(since we can(x * 2), (x * 3) and (x + 1) based on the requirments)
        interm1, interm2, interm3 = [float('inf')] * 3
        # calculate intem value for each allowed operation
        interm1 = num_operations[i - 1] + 1
        if i % 2 == 0:
            interm2 = num_operations[i // 2] + 1
        if i % 3 == 0:
            interm3 = num_operations[i // 3] + 1       
        # choose min num of operations from three available    
        min_ops = min(interm1, interm2, interm3)
        # assign min number of operations to the i-th elem
        num_operations[i] = min_ops   
    total_operations = num_operations[n]    

    # here we need to store all the interm values that we get during the calculation
    res = [n]
    while n > 1:
        if n % 2 == 0:
            n = n // 2
            res.append(n)
        if n % 3 == 0:
            n = n // 3
            res.append(n)
        else:
            n = n - 1
            res.append(n)   
    return total_operations, res[::-1]                

print(primitive_calculator(5))


