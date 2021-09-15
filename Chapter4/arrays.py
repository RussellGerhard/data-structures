from copy import deepcopy
"""
Implement a basic array object.
"""

class Array:
    """Represent an array."""

    def __init__(self, capacity = 5, fill_value = None):
        """
        Initialize array and fill each position with fill_value.

        deepcopy fill_value because, if it's mutable, each row in self.items
        will points to the same column object.
        """
        self.items = []
        self.logical_size = 0
        self.capacity = capacity
        self.default_capacity = capacity
        self.fill_value = fill_value
        for _ in range(capacity):
            self.items.append(deepcopy(fill_value))

    def __getitem__(self, index):
        """Get item at index in array."""
        if index < 0 or index >= self.size():
            raise IndexError("array index out of range")
        return self.items[index]

    def __iter__(self):
        """Support traversal with for loop."""
        return iter(self.items)
    
    def __len__(self):
        """Get capacity of array."""
        return self.capacity

    def __repr__(self):
        """Get representation of the array object."""
        return repr(self.items)

    def __setitem__(self, index, value):
        """Set value at index in array."""
        if index < 0 or index >= self.size():
            raise IndexError("array index out of range")
        self.items[index] = value

    def __str__(self):
        """Get string representation of the array object."""
        return str(self.items)

    def grow(self):
        """Double size of array."""
        if self.size() == len(self):
            # Double physical size
            temp = Array(len(self)*2)
            self.capacity = len(self)*2

            # Copy over items
            for i in range(self.size()):
                temp.items[i] = self.items[i]
            self.items = temp.items

    def insert(self, index, item):
        """Insert item in self before index position."""
        if index < 0:
            raise IndexError("array index must be nonnegative")
        else:
            # Grow if necessary
            self.grow()

            # Index larger than logical size, append at end
            if index >= self.size():
                self.items[self.size()] = item
            # Otherwise, copy elements and insert
            else:
                i = self.size()
                while i != index:
                    self.items[i] = self.items[i - 1]
                    i -= 1
                self[i] = item
            
            self.logical_size += 1

    def pop(self, index):
        """Take item at index in array out of the array and return it."""
        if index < 0 or index >= self.size():
            raise IndexError("array index out of range")
        else:
            i = index
            out = self.items[index]
            while i < self.size():
                self.items[i] = self.items[i + 1]
                i = i + 1

            # Shrink if necessary
            self.logical_size -= 1
            self.shrink()
            return out

    def remove(self, index):
        """Set item at index to default value."""
        if index < 0 or index >= self.size():
            raise IndexError("array index out of range")
        self.items[index] = self.fill_value

    def shrink(self):
        """Halve size of array."""
        if self.size() <= (len(self) // 4) and len(self) > (2 * self.default_capacity):
            # Halve physical size
            temp = Array(len(self) // 2)
            self.capacity = len(self) // 2

            # Copy over items
            for i in range(self.size()):
                temp.items[i] = self.items[i]
            self.items = temp.items

    def size(self):
        """Get logical size of array."""
        return self.logical_size

if __name__ == "__main__":
    a = Array(2)
    a.insert(0, 10)
    a.insert(1, 20)
    a.insert(2, 30)
    a.insert(3, 40)
    a.insert(4, 50)
