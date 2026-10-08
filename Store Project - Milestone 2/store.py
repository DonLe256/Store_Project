from customer import Customer
from product import Product

class Store:

    def __init__(self):
        self.customers = []
        self.products = []

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
