class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.hash = hash(key)


class Dictionary:
    def __init__(self):
        self.capacity = 0
        self.size = 0

    def __setitem__(self, key, value):
        ...

    def __getitem__(self, key):
        ...

    def __len__(self):
        return self.size

    def resize(self):
        ...

