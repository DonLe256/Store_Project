from linked_list import LinkedList


class OrderQueue():
    def __init__(self):
        self.queue = LinkedList()

    def enqueue(self, item):
        self.queue.add_last(item)

    def dequeue(self):
        return self.queue.remove_first()

    def peek(self):
        return self.queue.get_first()

    def is_empty(self):
        return self.queue.size() == 0

    def size(self):
        return self.queue.size()
    