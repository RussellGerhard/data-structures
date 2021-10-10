"""
Author:  Russell Gerhard
Purpose: Implement dictionary ADT using an array or a hash table.

Exports:    
    ArrayDict: Array implementation of dictionary.

    HashDict: Hash table implementation of dictionary.
"""

from dynamicarray import Array
from abstractclasses.abstractdict import Entry, AbstractDict

class ArrayDict(AbstractDict):
    """Implement dictionary using a dynamic array."""

    # Constructor
    def __init__(self, keys = None, values = None):
        """
        Instantiate self and initialize with keys and values from constructor
        arguments, if present.
        Precondition: keys and values must be iterables with same length
        Raises: ValueError
        """
        self.items = Array()
        AbstractDict.__init__(self, keys, values)
        

    # Accessors
    def __getitem__(self, key):
        """
        Return the value associated with key.
        Precondition: key must be in self.
        Raises: KeyError
        """
        if key not in self:
            raise KeyError(f"{key}")
        for entry in self.items:
            if entry.key == key:
                return entry.value

    def __iter__(self):
        """Return an iterator on the keys in self."""
        for entry in self.items:
            yield entry.key

    # Mutators
    def clear(self):
        """Remove every item in self and set length to 0."""
        self.length = 0
        self.items = Array()
        
    def pop(self, key, default_value = None):
        """
        If key is in self, remove it and return the associated value, else
        return default_value.
        """
        if key not in self:
            return default_value

        # Find index of entry to remove
        index = 0
        while index < len(self):
            if self.items[index].key == key:
                break
            index += 1

        # Save return value and copy over entry in self.items
        return_val = self.items[index].value
        index += 1
        while index < self.items.size():
            self.items[index - 1] = self.items[index]
            index += 1
        self.items[index - 1] = self.items.fill_value
        
        # Decrement length, as well as logical size of self.items
        # Shrink self.items if necessary
        self.length -= 1
        self.items.logical_size -= 1
        self.items.shrink()

        return return_val

    def __setitem__(self, key, value):
        """
        If key is in self, replace its value with the argument passed, else
        create a new key in self and associated the value argument with it.
        """
        index = 0
        while index < len(self):
            if self.items[index].key == key:
                self.items[index].value = value
                break
            index += 1

        # If key not in self
        if index == len(self):
            # Grow if necessary and add new entry
            self.items.grow()
            self.items[index] = Entry(key, value)

            # Increment length
            self.length += 1

class HashDict(AbstractDict):
    """Implement dictionary using a hash table."""

    def __init__(self, keys = None, values = None):
        """
        Instantiate self and initialize with keys and values from constructor
        arguments, if present.
        Precondition: keys and values must be iterables with same length
        Raises: ValueError
        """
