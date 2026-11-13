class Order():
    """
    After customers are done choosing products and are ready to be checked out,
    the items in the characters shopping cart become an order
    """
    def __init__(self, order_id, customer, items):
        """
        Creates an order with a given ID, the customer of the 
        order, and the items they are buying
        """
        self.order_id = order_id
        self.customer = customer
        self.items = items.copy()
        self.status = "PENDING"

    def get_id(self):
        """Returns the ID of the order"""
        return self.order_id

    def get_customer(self):
        """Returns the customer making the order"""
        return self.customer

    def get_items(self):
        """Returns all the products in the order as a list"""
        return self.items

    def get_status(self):
        """Returns the status of the customer's order"""
        return self.status

    def set_status(self, new_status):
        """Update the order status if the provided status is valid."""
        if new_status not in ["PENDING", "PROCESSING", "COMPLETED"]:
             pass
        self.status = new_status
            
    def calculate_total(self):
        """
        Adds together the prices of all the items in the 
        customer's order and returns the total
        """
        total = 0
        for i in self.items:
            total += i.get_price()
        return total
