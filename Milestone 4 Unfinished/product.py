class Product:

    """
    What the customer is buying and putting into their shopping cart
    """

    def __init__(self, id, name, price):
        """Creates a product with a given ID, Name, and price"""
        self.id = id
        self.name = name
        self.price = price

    def get_id(self):
        """Returns the ID of the product"""
        return self.id

    def get_name(self):
        """Returns the name of the product"""
        return self.name

    def get_price(self):
        """Returns the price of the product"""
        return self.price


