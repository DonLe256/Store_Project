from product import Product

class ShoppingCart:
    """Represents a shopping cart containing products."""
    def __init__(self):
        """Initialize an empty shopping cart."""
        self.items = []

    def is_empty(self):
        """Return True if the cart contains no products."""
        return len(self.items) == 0

    def add_product(self, product):
        """Add a product to the shopping cart."""
        self.items.append(product)

    def get_items(self):
        """Returns items in shopping cart"""
        return self.items

    def calculate_total(self):
        """Calcualtes the total price of all products in a cart"""
        total = 0
        for product in self.items:
            total += product.get_price()
        return total

    def remove_product(self,id):
        """Remove specific Product from cart"""
        for product in self.items:
            if product.get_id() == id:
                self.items.remove(product)
                return True
        return False

    def clear(self):
        """Remove all products from the shopping cart."""
        if len(self.items) == 0:
            pass
        while len(self.items) > 0:
            self.items.pop()
            



# mine = ShoppingCart()
# shirt = Product(10,"Shirt", 20)
# red = Product(4,"Paint",45)
# mine.add_product(shirt)
# mine.add_product(red)
# mine.add_product(shirt)
# print(mine.get_items())
# print(mine.calculate_total())
# mine.clear()
# print(mine.calculate_total())

# mine.remove_product(10)
# pint()
# print(mine.get_items())
# print(mine.calculate_total())
