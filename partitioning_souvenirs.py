def partitioning_souvenirs(n):
    # calculate sun of the elem
    sum = 0
    for i in range(len(n)):
        sum += n[i]
    # check if the sum is not divided evenly be the number of partitions,  
    # return 0, no need to do furtehr calculations 
    if sum % 3 != 0:
        return 0
    
    # calculate max amount for each partition 
    partition = sum / 3
    # create a matrix with matching to len(n) rows and partition number of columns
    T = [[0 for i in range(len(n) + 1)] for j in range(partition + 1)]
    # set each 0 column to be False
    for i in range(partition+1):
        T[i][0] = 0
    # set first 0 row to be True    
    for j in range(len(n)+1):
        T[0][j] = 1

    for i in range(1, partition+1):
        for j in range(1, len(n)+ 1):
            # set default value to be what one row abovw 
            T[i][j] = T[i][j-1]  
            # check if the souvenir value is less or equal to current i-th amount 
            if n[j-1] <= i:
                # assign bool value of the element one row above in the matrix minus elem j-th value 
                # or the current bool value
                res = T[i-n[j-1]][j-1] or T[i][j]
                T[i][j] = res     
    return T[partition][len(n)]            

print(partitioning_souvenirs([1, 1, 1]))
