
class Node():
    """
    Nodes are the components of the linked list
    """
    def __init__(self, item, link = None):
        """Initializes the item and link(if given) of nodes"""
        self.item = item
        self.link = link

    def __repr__(self):
        """Returns the item of the node as a string"""
        return f"Node({self.item})"