import algorithms
from customer import Customer
from product import Product
from order import Order
from cart import ShoppingCart
from store import Store
import unittest

class TestRecursiveTotalPrice(unittest.TestCase):
    """Tests the Recursive Total Price Method"""
    
    def setUp(self):
        self.shopping_list = ShoppingCart([Product(1, "Apple", 4.00), 
                        Product(2, "Banana", 2.00),
                        Product(3, "Pear", 4.00)])
    def test_Order_Total(self):
        "Test the Method with Different Lists of items"
        self.assertEqual(algorithms.recursive_total_price(self.shopping_list.get_items()),10)
        self.shopping_list.remove_product(1)
        self.shopping_list.remove_product(2)
        self.assertEqual(algorithms.recursive_total_price(self.shopping_list.get_items()),4)

    def test_empty_product_list(self):
        """Testing an empty cart"""
        self.assertEqual(algorithms.recursive_total_price([]),0)
        self.shopping_list.clear() #Emptying List
        self.assertEqual(algorithms.recursive_total_price(self.shopping_list.get_items()),0)





class TestFewestCoins(unittest.TestCase):
    "Tests the Fewest Coins Method"
    mycoins = [1,5,10,25]
    othercoins = [3,6,13]
    def test_Fewest_Coins(self):
        "Tests the Functionality of the Fewest Coins method"
        self.assertEqual(algorithms.fewest_coins(self.mycoins, 50),2)
        self.assertEqual(algorithms.fewest_coins(self.mycoins, 43),6)
        self.assertEqual(algorithms.fewest_coins(self.mycoins, 3),3)
        self.assertEqual(algorithms.fewest_coins(self.othercoins, 9),2)
        
    def test_Exact_Amount(self):
        self.assertEqual(algorithms.fewest_coins(self.mycoins, 25), 1)

    def test_NoAmount(self): 
        """Tests Method When Amount is 0"""
        self.assertEqual(algorithms.fewest_coins(self.mycoins, 0),0)

    def test_NoCoins(self):
        """Tests Method When Coin List is Empty"""
        self.assertEqual(algorithms.fewest_coins([], 3),-1)

    def test_NoSolution(self):
        """Tests Method When There is No Possible Solution for the Amount"""
        self.assertEqual(algorithms.fewest_coins(self.othercoins,7),-1)
    
class TestSorting(unittest.TestCase):
    """Tests sorting algorithms and their Store methods."""

    def setUp(self):
        self.store = Store()
        self.Apple, self.Banana, self.Pear = Product(3, "Apple", 4.00), Product(2, "Banana", 2.00), Product(1, "Pear", 4.00)
        self.store.add_product(self.Apple)
        self.store.add_product(self.Banana)
        self.store.add_product(self.Pear)
        self.expected_products = [self.Pear, self.Banana, self.Apple]

    def test_Bubble_Sorting(self):
        """Tests bubble sorting through Store."""
        products = self.store.products
        self.store.bubble_sort_products()
        self.assertIs(self.store.products, products)
        self.assertEqual(self.store.products, self.expected_products)

    def test_Selection_Sorting(self):
        """Tests selection sorting through Store."""
        products = self.store.products
        self.store.selection_sort_products()
        self.assertIs(self.store.products, products)
        self.assertEqual(self.store.products, self.expected_products)

    def test_Insertion_Sorting(self):
        """Tests insertion sorting through Store."""
        products = self.store.products
        self.store.insertion_sort_products()
        self.assertIs(self.store.products, products)
        self.assertEqual(self.store.products, self.expected_products)

    def test_Sorting_Algorithms(self):
        """Tests all three sorting algorithms directly"""
        products = [self.Banana, self.Apple, self.Pear]
        algorithms.bubble_sort(products)
        self.assertEqual(products, self.expected_products)

        products = [self.Banana, self.Apple, self.Pear]
        algorithms.selection_sort(products)
        self.assertEqual(products, self.expected_products)

        products = [self.Banana, self.Apple, self.Pear]
        algorithms.insertion_sort(products)
        self.assertEqual(products, self.expected_products)

    def test_Already_Sorted(self):
        """Tests all three algorithms on already sorted products."""
        products = [self.Pear, self.Banana, self.Apple]
        algorithms.bubble_sort(products)
        self.assertEqual(products, self.expected_products)

        products = [self.Pear, self.Banana, self.Apple]
        algorithms.selection_sort(products)
        self.assertEqual(products, self.expected_products)

        products = [self.Pear, self.Banana, self.Apple]
        algorithms.insertion_sort(products)
        self.assertEqual(products, self.expected_products)

    def test_Reverse_Sorted(self):
        """Tests all three algorithms on reverse sorted products."""
        products = [self.Apple, self.Banana, self.Pear]
        algorithms.bubble_sort(products)
        self.assertEqual(products, self.expected_products)

        products = [self.Apple, self.Banana, self.Pear]
        algorithms.selection_sort(products)
        self.assertEqual(products, self.expected_products)

        products = [self.Apple, self.Banana, self.Pear]
        algorithms.insertion_sort(products)
        self.assertEqual(products, self.expected_products)

    def test_Empty_List(self):
        """Tests all three algorithms with no products."""
        products = []
        algorithms.bubble_sort(products)
        self.assertEqual(products, [])

        products = []
        algorithms.selection_sort(products)
        self.assertEqual(products, [])

        products = []
        algorithms.insertion_sort(products)
        self.assertEqual(products, [])

    def test_One_Product(self):
        """Tests all three algorithms with one product."""
        products = [self.Apple]
        algorithms.bubble_sort(products)
        self.assertEqual(products, [self.Apple])

        products = [self.Apple]
        algorithms.selection_sort(products)
        self.assertEqual(products, [self.Apple])

        products = [self.Apple]
        algorithms.insertion_sort(products)
        self.assertEqual(products, [self.Apple])

class TestBinarySearch(unittest.TestCase):
    """Test Binaray Search Algorithm"""
    def setUp(self):
        """Set up for Current method"""
        self.shopping_list = ShoppingCart([Product(i, str(i), i) for i in range(20)])

    def test_seach(self):
        """Test Binary search on inputs"""
        self.assertEqual((algorithms.binary_search(self.shopping_list.get_items(),10)),10)
        self.assertEqual((algorithms.binary_search(self.shopping_list.get_items(),9)),9)
        self.assertEqual((algorithms.binary_search(self.shopping_list.get_items(),15)),15)

    def test_first_item(self):
        """Tests Binary Seach Method for the first item in a list"""
        self.assertEqual((algorithms.binary_search(self.shopping_list.get_items(),0)),0)

    def test_middle_item(self):
        """Tests Binary Search for middle item"""
        self.assertEqual((algorithms.binary_search(self.shopping_list.get_items(),10)),10)

    def test_not_found(self):
        """Tests Binary Search method when item is not in list"""
        self.assertEqual((algorithms.binary_search(self.shopping_list.get_items(),21)),-1)
        self.assertEqual((algorithms.binary_search(self.shopping_list.get_items(),-1)),-1)
        self.assertEqual((algorithms.binary_search(self.shopping_list.get_items(),-100)),-1)

    def test_empty_list(self):
        """Tests Binary Search on an empty list"""
        self.assertEqual(algorithms.binary_search([], 5), -1)

class TestStoreIntegration(unittest.TestCase):
    """Tests Store methods that use algorithms.py."""
    def setUp(self):
        self.store = Store()
        self.apple = Product("P300", "Apple", 4.00)
        self.banana = Product("P100", "Banana", 2.00)
        self.pear = Product("P200", "Pear", 4.00)
        self.store.add_product(self.apple)
        self.store.add_product(self.banana)
        self.store.add_product(self.pear)

    def test_binary_search_product(self):
        """Tests searching for existing and missing products"""
        self.store.insertion_sort_products()
        self.assertIs(self.store.binary_search_product("P100"), self.banana)
        self.assertIs(self.store.binary_search_product("P200"), self.pear)
        self.assertIsNone(self.store.binary_search_product("P999"))

    def test_recursive_catalog_total(self):
        """Tests calculating the total price of the catalog"""
        self.assertEqual(self.store.recursive_catalog_total(), 10.00)
        empty_store = Store()
        self.assertEqual(empty_store.recursive_catalog_total(), 0.0)

    def test_calculate_change(self):
        """Tests calculating the minimum number of coins"""
        self.assertEqual(self.store.calculate_change([1, 5, 10], 12), 3)
        self.assertEqual(self.store.calculate_change([1, 5, 10], 0), 0)
        self.assertEqual(self.store.calculate_change([3, 6, 13], 9), 2)
        
if __name__ == "__main__":
    unittest.main()
