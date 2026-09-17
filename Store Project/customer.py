import ShoppingCart

class Customer(ShoppingCart):

    def __init__(self, name):
        super().__init__(self, cart = [])
        self.name = name

    def __str__(self):
        return f"{self.name} is here to shop."

    def add_to_cart(item):
        