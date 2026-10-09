from customer import Customer
from product import Product
from order_queue import OrderQueue
from stack import Stack
from order import Order

class Store:
    """Allows to manage the stores products, customers, and orders."""
    def __init__(self):
        """Initialize the store and its data structures"""
        self.customers = []
        self.products = []
        self.orders_list = []
        self.queue = OrderQueue()
        self.processed_orders = Stack()
        self.order_counter = 0

    def add_customer(self, customer):
         """Add a customer if their ID is not already registered"""
         if self.find_customer(customer.get_id()) != None:
             return False
         self.customers.append(customer)
         return True

    def add_product(self, product):
        """Add a product if its id is not already registered"""
        if self.find_product(product.get_id()) != None:
            return False
        self.products.append(product)
        return True

    def find_customer(self, id):
        """Find and return a customer by ID"""
        for customer in self.customers:
            if customer.get_id() == id:
                return customer
        return None

    def find_product(self,id): 
        """Find and return a product by ID"""
        for product in self.products: 
            if product.get_id() == id:
                return product
        return None

    def find_order(self, id):
        """Find and return an order by ID."""
        for i in self.orders_list:
            if id == i.get_id():
                return i
        return None

    def get_orders(self):
        """Return all orders placed in the store."""
        return self.orders_list

    def checkout(self, id):
        """Create an order from a customer's cart and queue it for processing."""
        customer = self.find_customer(id)
        if customer is None or not(customer.get_cart().get_items()):
            return None
        self.order_counter += 1
        order_id = f"O{self.order_counter}"
        new_order = Order(order_id, customer, customer.get_cart().get_items())  
        self.orders_list.append(new_order)
        self.queue.enqueue(new_order)
        customer.get_cart().clear()
        return new_order

    def process_next_order(self):
        """Process the oldest waiting order and add it to the history stack."""
        if self.queue.size() == 0:
            return None
        order_to_be_processed = self.queue.dequeue()
        order_to_be_processed.set_status("PROCESSING")
        self.processed_orders.push(order_to_be_processed)
        return order_to_be_processed

    def get_order_history(self):
        """Return processed orders from newest to oldest."""
        history = []
        temp = Stack()
        while not self.processed_orders.is_empty():
            order = self.processed_orders.pop()
            history.append(order)
            temp.push(order)
        while not temp.is_empty():
            self.processed_orders.push(temp.pop())
        return history