import sys


class MemCalc:

    def __init__(self):
        self.used_memory = 0
        self.registered_objects = set()

    def add(self, x):
        object_id = id(x)
        if object_id not in self.registered_objects:
            self.registered_objects.add(object_id)
            self.used_memory += sys.getsizeof(x)
            if hasattr(x, '__iter__'):
                if hasattr(x, 'item'):
                    x = x.items()
                for xx in x:
                    self.add(xx)

    def get_used_memory(self):
        return self.used_memory
