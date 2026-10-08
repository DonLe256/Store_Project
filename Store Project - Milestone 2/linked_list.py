from node import Node


class LinkedList():
    def __init__(self, items):
        self._head = None
        self._tail = None
        self._len = 0

        if self.items is not None:
            for item in items:
                pass

    def __len__(self):
        return self._len

    def get_first(self):
        if self._head is None:
            return None
        return self._head.item

    def add_first(self, item):
        self._tail = Node(item, self._head)
        self._len += 1
        if self._len == 1:
            self._tail = self._head

    def add_last(self, item):
        if self._len == 0:
            return self.add_first(item)
        else:
            self._tail.link = Node(item)
            self._tail.link = self._tail
        self._len += 1

    def remove_first(self):
        if self._len == 0:
            raise RuntimeError
        removed_item = self._head.item
        self._head = self._head.link
        if self._len == 0:
            self._tail = None
        self._len -= 1
        return removed_item
            

    def remove_last(self):
        if self._len == 0:
            raise RuntimeError
        if self._len == 1:
            return self.remove_first()
        removed_data = self._tail.data
        temp = self._head
        while temp.link.link is not None:
            temp = self._head.link
        temp.link = None
        self._tail = temp
        self._len -= 1
        return removed_data

    def size(self):
        return self._len

    

