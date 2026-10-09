from customer import Customer
from product import Product


from order import Order
from linked_list import LinkedList
from stack import Stack
from order_queue import OrderQueue
from store import Store
import unittest

class TestOrder(unittest.TestCase):
    def test_init(self):
        c1 = Customer(1, "John")
        shopping_list = [Product(1, "Apple", 4.00), 
                         Product(2, "Banana", 2.00),
                         Product(3, "Pear", 4.00)]
        order1 = Order(1, c1, shopping_list)
        self.assertEqual(order1.order_id, 1)
        self.assertEqual(order1.items, shopping_list)
        self.assertEqual(order1.customer, c1)
    def test_innit(self):
        c1 = Customer(1, "John")
        shopping_list = [Product(1, "Apple", 4.00), 
                         Product(2, "Banana", 2.00),
                         Product(3, "Pear", 4.00)]
        order1 = Order(1, c1, shopping_list)
        self.assertEqual(order1.calculate_total(), 10.00)


class TestLinkedList(unittest.TestCase):
    def test_add_first(self):
        L1 = LinkedList()
        items = [2, 4, 6, 8]
        for i in range(len(items)):
            self.assertEqual(L1.size(), i)
            L1.add_first(items[i])
            self.assertEqual(L1.get_first(), items[i])

    def test_add_last(self):
        L1 = LinkedList()
        items = [2, 4, 6, 8]
        for i in range(len(items)):
            self.assertEqual(L1.size(), i)
            L1.add_first(items[i])

class TestStack(unittest.TestCase):
    pass

class TestOrderQueue(unittest.TestCase):
    pass

class TestStore(unittest.TestCase):
    pass



if __name__ == "__main__":
    unittest.main()