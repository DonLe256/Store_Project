def recursive_total_price(products):
    """
    Uses recursion to add together all the prices of products.
    Ends when the length of the given list of products reaches 1.
    """
    if products is None or len(products) == 0:
        return 0
    if len(products) == 1:
        return products[0].get_price()
    return products[0].get_price() + recursive_total_price(products[1:len(products)])

def fewest_coins(coins, amount):
    """
    Returns the minimum number of coins needed to make an amount.
    Returns -1 if no combination is possible.
    """
    if amount == 0:
        return 0
    if coins == []:
        return -1
    solved = {coin: 1 for coin in coins}
    result = _fewest_coins(coins, amount, solved)
    if result == float('inf'):
        return -1
    return result

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

def bubble_sort(products):
    """
    Compares each product's id with the product's next to it and
    swaps them if they have greater unicode value.
    """
    n = len(products)
    for i in range(n-1):
        made_swaps = False

        for j in range(n - 1 - i):
            if products[j].get_id() > products[j + 1].get_id():
                made_swaps = True
                products[j], products[j + 1] = products[j + 1], products[j]

        if not made_swaps:
            break

def selection_sort(products):
    """
    Finds the product with the greatest id value, and swaps it to the
    end of the sub-list.
    """
    n = len(products)
    for i in range(n-1):
        index_max = 0
        product_max = products[index_max].get_id()

        for j in range(n-i):
            if products[j].get_id() > product_max:
                index_max = j
                product_max = products[index_max].get_id()
                
        products[j], products[index_max] = products[index_max], products[j]

def insertion_sort(products):
    """
    Compares a product's id from the beginning of a sub-list to elements
    next to it. 
    Moves the element to the right if larger than the next element.
    """
    n = len(products)

    for i in range(n-1):
        j = n - 2 - i
        product = products[j]

        while j < n-1 and product.get_id() > products[j+1].get_id():
            products[j] = products[j+1]
            j += 1

        products[j] = product


def binary_search(products, product_id):
    """
    The publically executable function for the binary search.
    Only the list of products and id of the product being searched for are needed this way.
    """
    return _binary_search(product_id, products, left = 0, right = len(products), i_first = -1)

def _binary_search(product_id, products, left, right, i_first):
    """
    Helper method for binary search algorithm.

    Uses recursion to compare the median and target and 
    change the bounds of the search every recursive step.

    Returns -1 if the item is not found and the index if the item is found.
    """
    if right - left == 0:
        return i_first

    if products[left].get_id() == product_id:
        i_first = left

    if right-left == 1:
        return i_first

    median = (right+left)//2

    if products[median].get_id() > product_id:
        return _binary_search(product_id, products, left, median, i_first)

    elif products[median].get_id() < product_id:
        return _binary_search(product_id, products, median, right, i_first)

    elif left != median:
        i_first = median
        return _binary_search(product_id, products, left, median, i_first)
        
