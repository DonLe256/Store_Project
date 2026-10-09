from linked_list import LinkedList

class Stack():
    """A stack implemented using a linked list."""
    def __init__(self):
        """Initialize an empty stack."""
        self._L = LinkedList()

    def push(self, item):
        """Add an item to the top of the stack."""
        self._L.add_first(item)

    def pop(self):
        """Remove and return the top item."""
        return self._L.remove_first()

    def peek(self):
        """Return the top item without removing it."""
        return self._L.get_first()

    def __len__(self):
        """Return the number of items in the stack using len()."""
        return len(self._L)

    def is_empty(self):
        """Return True if the stack is empty."""
        return self._L.is_empty()

    def size(self):
        """Return the number of items in the stack."""
        return self._L.size()