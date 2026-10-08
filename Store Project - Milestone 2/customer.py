from cart import ShoppingCart
class Customer:

    def __init__(self, ID , name):
        self.ID = ID
        self.name = name
        self.cart = ShoppingCart()

    def get_id(self):
        return self.ID

    def get_name(self):
        return self.name

    def get_cart(self):
        return self.cart


test = Customer(5, "logan")