import operator 

# that's needed to turn string into operator, e.g. "+" into operator +
ops = {
   "+": operator.add,
   "-": operator.sub,
   "*": operator.mul
}

# function that will return min and max values 
def min_and_max(i, j, min_matrix, max_matrix, operations):
    min_value = float('inf')
    max_value = float('-inf')
    for k in range(i, j):
        a = ops[operations[k-1]](max_matrix[i][k], max_matrix[k+1][j]) 
        b = ops[operations[k-1]](max_matrix[i][k], min_matrix[k+1][j]) 
        c = ops[operations[k-1]](min_matrix[i][k], min_matrix[k+1][j]) 
        d = ops[operations[k-1]](min_matrix[i][k], max_matrix[k+1][j])
        min_value = min(min_value, a, b, c, d)
        max_value = max(max_value, a, b, c, d)   

    return (min_value, max_value)  




def get_maximum_value(digits, operations):
    n = len(digits)
    print(n, 'n')
    # initialize matrix that will store min vlaues
    min_matrix = [[0 for i in range(n+1)] for _ in range(n+1)]
    # initialize matrix that will store max vlaues
    max_matrix = [[0 for i in range(n+1)] for _ in range(n+1)]

    
    # insert digits from the expression in the matrix diagonale, from that diagonale we will start calculating results 
    for i in range(1, len(max_matrix)):
        min_matrix[i][i] = digits[i-1]
        max_matrix[i][i] = digits[i-1]        

    for s in range(1, n):
        for i in range(1, n + 1 - s):
            j = i + s
            min_matrix[i][j], max_matrix[i][j] = min_and_max(i, j, min_matrix, max_matrix, operations)

    return max_matrix[1][n]        
       

if __name__ == '__main__':
    expression = "5 - 8 + 7 * 4 - 8 + 9"
    # remove empty spaces in the string if there are some
    expression = "".join(expression.split())
    print(expression, 'expression')
    digits = [int(expression[i]) for i in range(0, len(expression), 2)]
    operations = [expression[i] for i in range(1, len(expression), 2)]
    print(get_maximum_value(digits, operations))
    # expected 200