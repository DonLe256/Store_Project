class Order():
    def __init__(self, order_id, customer, items):
        self.order_id = order_id
        self.customer = customer
        self.items = items
        self.status = "PENDING"

    def get_id(self):
        return self.order_id

    def get_customer(self):
        return self.customer

    def get_items(self):
        return self.items

    def get_status(self):
        return self.status

    def set_status(self, new_status):
        if new_status not in ["PENDING", "PROCESSING", "COMPLETED"]:
            pass
        self.status = new_status

    def calculate_total(self):
        total = 0
        for i in self.items:
            total += i.get_price()
        return total
