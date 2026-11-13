from node import Node


class LinkedList():
    """
    Data structure class used to create abstract data
    types such as queues and stacks
    """
    def __init__(self, items = None):
        """
        Establishes a head and tail component, length, and if initialized
        with a given list of items, all items will be added to the end of the linked list
        """
        self._head = None
        self._tail = None
        self.items = items
        self._len = 0

        if self.items is not None:
            for item in items:
                self.add_last(item)

    def __len__(self):
        """Gives the length of the linked list"""
        return self._len

    def get_first(self):
        """
        If the length of the list is 0/there is no head then None will be returned,
        otherwise the item of the head of the list will be returned
        """
        if self._head is None:
            return None
        return self._head.item

    def get_last(self):
        """
        If the length of the list is 0/there is no tail then None will be returned,
        otherwise the item of the tail of the list will be returned
        """
        if self._tail is None:
            return None
        return self._tail.item

    def add_first(self, item):
        """Creates a new node with the given item and adds it to the beginning"""
        self._head = Node(item, self._head)
        self._len += 1
        if self._len == 1:
            self._tail = self._head

    def add_last(self, item):
        """Creates an new node with the given item and adds it to the end"""
        if self._len == 0:
            return self.add_first(item)
        else:
            self._tail.link = Node(item)
            self._tail = self._tail.link
        self._len += 1

    def remove_first(self):
        """Removes the first node / the head in the linked list"""
        if self._len == 0:
            return None
        removed_item = self._head.item
        self._head = self._head.link
        self._len -= 1
        if self._len == 0:
            self._tail = None
        return removed_item
            

    def remove_last(self):
        """Removes the last node / the tail in the linked list"""
        if self._len == 0:
            return None
        if self._len == 1:
            return self.remove_first()
        removed_item = self._tail.item
        temp = self._head
        while temp.link is not self._tail:
            temp = temp.link
        temp.link = None
        self._tail = temp
        self._len -= 1
        return removed_item

    def size(self):
        """Gives the length of the linked list"""
        return self._len
    
    def is_empty(self):
        """Determines whether or not the list is empty"""
        return self._len == 0

    

