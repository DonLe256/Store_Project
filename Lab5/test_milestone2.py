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
        c1 = Customer("C1", "John")
        shopping_list = [Product("P1", "Apple", 4.00),
                         Product("P2", "Banana", 2.00),
                         Product("P3", "Pear", 4.00)]
        order1 = Order("O1", c1, shopping_list)
        self.assertEqual(order1.get_id(), "O1")
        self.assertEqual(order1.get_items(), shopping_list)
        self.assertIs(order1.get_customer(), c1)
        self.assertEqual(order1.get_status(), "PENDING")
        shopping_list.clear()
        self.assertEqual(len(order1.get_items()), 3)

    def test_total(self):
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
            L1.add_last(items[i])
        self.assertEqual(L1.get_first(), 2)
        self.assertEqual([L1.remove_first() for _ in items], items)

    def test_empty(self):
        L1 = LinkedList()
        self.assertTrue(L1.is_empty())
        self.assertIsNone(L1.get_first())
        self.assertIsNone(L1.remove_first())
        L1.add_first(2)
        self.assertFalse(L1.is_empty())
        self.assertEqual(L1.remove_first(), 2)
        self.assertTrue(L1.is_empty())

    def test_remove_first(self):
        L1 = LinkedList()
        L1.add_last(2)
        L1.add_last(4)
        self.assertEqual(L1.remove_first(), 2)
        self.assertEqual(L1.get_first(), 4)
        self.assertEqual(L1.size(), 1)

class TestStack(unittest.TestCase):
    def test_lifo(self):
        stack = Stack()
        stack.push(2)
        stack.push(4)
        stack.push(6)
        self.assertEqual(stack.size(), 3)
        self.assertEqual(stack.pop(), 6)
        self.assertEqual(stack.pop(), 4)
        self.assertEqual(stack.pop(), 2)

    def test_peek(self):
        stack = Stack()
        stack.push(2)
        stack.push(4)
        self.assertEqual(stack.peek(), 4)
        self.assertEqual(stack.size(), 2)
        self.assertEqual(stack.pop(), 4)

    def test_empty(self):
        stack = Stack()
        self.assertTrue(stack.is_empty())
        self.assertIsNone(stack.pop())
        self.assertIsNone(stack.peek())
        stack.push(2)
        self.assertFalse(stack.is_empty())

class TestOrderQueue(unittest.TestCase):
    def test_fifo(self):
        queue = OrderQueue()
        queue.enqueue(2)
        queue.enqueue(4)
        queue.enqueue(6)

        self.assertEqual(queue.size(), 3)
        self.assertEqual(queue.dequeue(), 2)
        self.assertEqual(queue.dequeue(), 4)
        self.assertEqual(queue.dequeue(), 6)

    def test_peek(self):
        queue = OrderQueue()
        queue.enqueue(2)
        queue.enqueue(4)

        self.assertEqual(queue.peek(), 2)
        self.assertEqual(queue.size(), 2)
        self.assertEqual(queue.dequeue(), 2)

    def test_empty(self):
        queue = OrderQueue()
        self.assertTrue(queue.is_empty())
        self.assertIsNone(queue.dequeue())
        self.assertIsNone(queue.peek())
        queue.enqueue(2)
        self.assertFalse(queue.is_empty())

class TestStore(unittest.TestCase):
    def test_checkout(self):
        store = Store()
        customer = Customer("C1", "John")
        apple = Product("P1", "Apple", 4.00)

        store.add_customer(customer)
        customer.get_cart().add_product(apple)

        order = store.checkout("C1")

        self.assertEqual(order.get_id(), "O1")
        self.assertEqual(order.get_status(), "PENDING")
        self.assertEqual(order.get_items(), [apple])
        self.assertTrue(customer.get_cart().is_empty())
        self.assertEqual(store.get_orders(), [order])

    def test_process_next_order(self):
        store = Store()
        customer = Customer("C1", "John")
        store.add_customer(customer)

        customer.get_cart().add_product(Product("P1", "Apple", 4.00))
        first = store.checkout("C1")

        customer.get_cart().add_product(Product("P2", "Pear", 5.00))
        second = store.checkout("C1")

        self.assertIs(store.process_next_order(), first)
        self.assertEqual(first.get_status(), "PROCESSING")

        self.assertIs(store.process_next_order(), second)
        self.assertEqual(second.get_status(), "PROCESSING")

        self.assertIsNone(store.process_next_order())

    def test_history(self):
        store = Store()
        customer = Customer("C1", "John")
        store.add_customer(customer)

        customer.get_cart().add_product(Product("P1", "Apple", 4.00))
        first = store.checkout("C1")

        customer.get_cart().add_product(Product("P2", "Pear", 5.00))
        second = store.checkout("C1")

        store.process_next_order()
        store.process_next_order()

        self.assertEqual(store.get_order_history(), [second, first])
        self.assertEqual(store.get_order_history(), [second, first])



if __name__ == "__main__":
    unittest.main()