from linked_list import LinkedList

class Stack():
    def __init__(self):
        self._L = LinkedList()

    def push(self, item):
        self._L.add_last(item)

    def pop(self):
        return self._L.remove_last()

    def peek(self):
        return self._L.get_last()

    def __len__(self):
        return len(self._L)

    def isempty(self):
        return len(self._L) == 0