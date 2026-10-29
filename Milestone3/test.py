def fewest_coins(coins, amount):
    """ 
    Initializes a new dictionary for each new function call.
    """
    solved = {coin:1 for coin in coins}
    print(solved)
    return _fewest_coins(coins, amount, solved)

def _fewest_coins(coins, amount, solved):
    """
    Helper method for fewer_coins algorithm.

    Finds the minimum amount of coins needed to give the customer back their change
    by going through all branches of coin combinations in order to find the branch that
    results in the least amount of coins needed.
    """
    if amount in solved:
        return solved[amount]
    elif amount == 0:
        return 0
    
    solved[amount] = float('inf')
    for coin in coins:
        if coin < amount:
            coins_branch = 1 + _fewest_coins(coins, amount - coin, solved)
            if coins_branch < solved[amount]:
                solved[amount] = coins_branch

    return solved[amount]


def min_steps(steps, target):
    """Returns the minimum number of moves needed
    to reach target using the allowed steps."""
    solved = {step:1 for step in steps}
    return _min_steps(steps, target, solved)

def _min_steps(steps, target, solved,path=None):
    """Recursive helper function using memoization."""
    if path is None: path = []
    if target in solved:
        path + [target]
        return (solved[target]) 
    if target == 0:
        return 0
    solved[target] = float('inf')
    for step in steps:
        if step < target:
            step_total = 1 + _min_steps(steps,target - step, solved)
            if step_total < solved[target]:
                solved[target] = step_total
                bestpath = path
    return solved[target]
        


# moves = [2,3,7]
# print(min_steps(moves,12))

mycoins = [1,5,10,20]
mycoins2 = [1,5,10,25,35]
othercoins = [3,6,13]
print(fewest_coins(mycoins, 50))
print(fewest_coins(mycoins2, 50))
print(fewest_coins(othercoins, 7))
# mymem = {mycoins:1 for mycoins in mycoins}
# print(mymem)
