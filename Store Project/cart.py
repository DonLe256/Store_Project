class ShoppingCart():
    def __init__(self):
        self.cart = []

    def __str__(self):
        if self.cart == False:
            return "Your shopping cart is empty."
        else:
            for item in self.cart:
                return item
