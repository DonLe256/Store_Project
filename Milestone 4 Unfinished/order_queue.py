from linked_list import LinkedList

"""
- A queue implemented using the linked list data structure
- The OrderQueue creates a queue where orders a lined up before being checked out
"""

class OrderQueue():
    def __init__(self):
        """Creates a queue for orders using an empty linked list as the data structure"""
        self.queue = LinkedList()

    def enqueue(self, item):
        """Adds an order to the end of the queue"""
        self.queue.add_last(item)

    def dequeue(self):
        """Removes the order at the front of the queue"""
        return self.queue.remove_first()

    def peek(self):
        """Returns the order that is at the beginning of the queue"""
        return self.queue.get_first()

    def is_empty(self):
        """Determines whether or not the queue is empty"""
        return self.queue.size() == 0

    def size(self):
        """Returns the number of orders in the queue"""
        return self.queue.size()
    