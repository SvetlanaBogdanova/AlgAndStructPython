class PriorityQueue:
    def __init__(self, value_mapper=lambda x: x):
        self.root = None
        self.mapper = value_mapper

    def push(self, data):
        new_node = QueueNode(data)
        value = self.mapper(data)
        current, previous = self.root, None
        while current is not None and value > self.mapper(current.data):
            previous = current
            current = current.next
        if previous is None:
            new_node.next = self.root
            self.root = new_node
        else:
            previous.next, new_node.next = new_node, previous.next

    def pop(self):
        lowest = self.root
        self.root = None if lowest is None else lowest.next
        return None if lowest is None else lowest.data


class QueueNode:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
