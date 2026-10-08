from linked_list import linked_list

class Stack():
    def __init__(self):
        self._L = linked_list()

    def push(self, item):
        self._L.add_last(item)

    def pop(self):
        return self._L.remove_last()

    def peek(self):
        return self._L.get_tail()

    def __len__(self):
        return len(self._L)

    def isempty(self):
        return len(self._L) == 0