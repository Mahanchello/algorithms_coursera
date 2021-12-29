# get change using dynamic programming algorithm (we use bottom-up approach)
# coins denominations are 1, 3, 4
# Note: to solve this problem, we do not need to use Greedy algorithm
# we use python's float["inf"] as an unbounded upper value for comparison.
# This is useful for finding lowest value for something. 
# for example, calculating path route costs when traversing trees.
# in simple words float("inf") is used to set up a var with infinite large value.

def dp_change(money, coins):
    # define an array of infinite large values
    min_coins = [float("inf")]*(money + 1)
    # set the first elem to be zero, because we will count from it later on line 22 (otherwise inf + int will return inf, but we need number)
    min_coins[0] = 0
    # handle the case when the money change match the coin
    if money in coins:
        return 1
    # loop through the money amount, starting from 1 (again we don't count from 0)
    for i in range(1, money + 1):
        # loops through coins 
        for coin in coins:
            # compare each elem of monaey change to the coin, and if it's more than or equal
            if i >= coin:
                # assign number of coins to the amount of previous coin + 1
                num_coins = min_coins[i - coin] + 1
                # to not override last elem in the num_coins array, adding this if statement to check 
                if num_coins < min_coins[i]:
                    min_coins[i] = num_coins
    return min_coins[money] 


print(dp_change(4, [1, 3, 4]))  





