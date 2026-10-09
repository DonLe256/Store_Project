from customer import Customer
from product import Product
from order_queue import OrderQueue
from stack import Stack
from order import Order

class Store:

    def __init__(self):
        self.customers = []
        self.products = []
        self.orders_list = []
        self.queue = OrderQueue()
        self.processed_orders = Stack()
        self.order_counter = 0

    def add_customer(self, customer):
         if self.find_customer(customer.get_id()) != None:
             return False
         self.customers.append(customer)
         return True

    def add_product(self, product):
        if self.find_product(product.get_id()) != None:
            return False
        self.products.append(product)
        return True

    def find_customer(self, id):
        for customer in self.customers:
            if customer.get_id() == id:
                return customer
        return None

    def find_product(self,id): 
        for product in self.products: 
            if product.get_id() == id:
                return product
        return None

    def find_order(self, id):
        for i in self.orders_list:
            if id == i.get_id():
                return i
        return None

    def get_orders(self):
        return self.orders_list

    def checkout(self, id):
        customer = self.find_customer(id)
        if customer is None or not(customer.get_cart().get_items()):
            return None
        
        new_order = Order(id, customer, customer.get_cart().get_items())
        self.orders_list.append(new_order)
        self.queue.enqueue(new_order)
        customer.get_cart().clear()
        return new_order

    def process_next_order(self):
        if self.queue.size() == 0:
            return None
        order_to_be_processed = self.queue.dequeue()
        order_to_be_processed.set_status("PROCESSING")
        self.processed_orders.push(order_to_be_processed)
        return order_to_be_processed

    def get_order_history(self):
        pass

    
