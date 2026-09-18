from product import Product

class ShoppingCart:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def add_product(self, product):
        self.items.append(product)

    def get_items(self):
        return self.items

    def calculate_total(self):
        total = 0
        for product in self.items:
            total += product.get_price()
        return total

    def remove_product(self,id):
        for product in self.items:
            if product.get_id() == id:
                self.items.remove(product)
                return True
        return False
            



# mine = ShoppingCart()
# shirt = Product(10,"Shirt", 20)
# red = Product(4,"Paint",45)
# mine.add_product(shirt)
# mine.add_product(red)
# mine.add_product(shirt)
# print(mine.get_items())
# print(mine.calculate_total())

# mine.remove_product(10)
# pint()
# print(mine.get_items())
# print(mine.calculate_total())
