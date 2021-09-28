"""
Author:  Russell Gerhard
Purpose: Implement a basic array object.

Exports:
    Array: Array that mimics functionality of explicity-memory-allocated arrays.
"""

from copy import deepcopy


class Array:
    """Represent an array."""
    default_capacity = 10

    def __init__(self, capacity = 10, fill_value = None):
        """
        Initialize array and fill each position with fill_value.
        deepcopy fill_value in case its mutable.
        """
        self.items = []
        self.logical_size = 0
        self.capacity = capacity
        self.default_capacity = capacity
        self.fill_value = fill_value
        for _ in range(capacity):
            self.items.append(deepcopy(fill_value))

    # Accessors
    def __eq__(self, other):
        """Return True if other is an array of same logical size and contents."""
        if self is other:
            return True
        elif type(other) != type(self):
            return False
        elif other.size() != self.size():
            return False
        else:
            i = 0
            while i < self.size():
                if self.items[i] != other.items[i]:
                    return False
                i += 1
            return True
            
    def __getitem__(self, index):
        """
        Return item at index in array.
        Precondition: Index in range(0, self.size())
        Raises: IndexError
        """
        if index < 0 or index >= self.size():
            raise IndexError("array index out of range")
        return self.items[index]

    def __iter__(self):
        """Support traversal with for loop."""
        return iter(self.items[:self.size()])
    
    def __len__(self):
        """Get capacity of array."""
        return self.capacity

    def __repr__(self):
        """Get representation of the array object."""
        return repr(self.items[:self.size()])

    def size(self):
        """Get logical size of array."""
        return self.logical_size

    def __str__(self):
        """Get string representation of the array object."""
        return str(self.items[:self.size()])
        
    # Mutators
    def grow(self):
        """Double capacity of array if logical size equals capacity."""
        if self.size() == len(self):
            # Double physical size
            temp = Array(len(self)*2)
            self.capacity = len(self)*2

            # Copy over items
            for i in range(self.size()):
                temp.items[i] = self.items[i]
            self.items = temp.items

    def insert(self, index, item):
        """
        Insert item in self before index position.
        Precondition: Index is nonnegative.
        Raises: IndexError
        """
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
        """
        Take item at index in array out of the array and return it.
        Precondition: Index in range(0, self.size())
        Raises: IndexError
        """
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

    def remove(self, item):
        """
        Remove first occurence of item in self.
        Precondition: item must be in self.
        Raises: KeyError
        """
        i = 0
        while i < self.size():
            if item == self[i]:
                break
            i += 1
        if i == self.size():
            raise KeyError("Array.remove(x): x not in array")
        else:
            i += 1
            while i != self.size():
                self[i - 1] = self[i]
                i += 1

        # Shrink if necessary
        self.logical_size -= 1
        self.shrink()
    
    def __setitem__(self, index, value):
        """
        Set value at index in array.
        Precondition: Index in range(0, self.size())
        Raises: IndexError
        """
        if index < 0 or index >= len(self):
            raise IndexError("array index out of range")
        self.items[index] = value
        if index >= self.size():
            self.logical_size = index + 1

    def shrink(self):
        """
        Halve capacity of array if logical size is less than or equal to a fourth of capacity
        and capacity is twice the default capacity.
        """
        if self.size() <= (len(self) // 4) and len(self) >= (2 * self.default_capacity):
            # Halve physical size
            temp = Array(len(self) // 2)
            self.capacity = len(self) // 2

            # Copy over items
            for i in range(self.size()):
                temp.items[i] = self.items[i]
            self.items = temp.items
