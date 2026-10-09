class Node():
    def __init__(self, item, link = None):
        self.item = item
        self.link = link

    def __repr__(self):
        return f"Node({self.item})"