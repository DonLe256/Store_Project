

from cart import ShoppingCart

class Customer:
    """Blueprints for a customer with and ID, name, and shopping cart"""
    def __init__(self, ID , name):
        """Initializes the ID and name of the customer and gives them and empty shopping cart"""
        self.ID = ID
        self.name = name
        self.cart = ShoppingCart()

    def get_id(self):
        """Gives the ID of the customer"""
        return self.ID

    def get_name(self):
        """Gives the name of the customer"""
        return self.name

    def get_cart(self):
        """Gives the customer's shopping cart as an object"""
        return self.cart


test = Customer(5, "logan")