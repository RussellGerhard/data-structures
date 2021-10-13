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
            raise KeyError(str(key))
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

    def __setitem__(self, key, new_value):
        """
        If key is in self, replace its value with the argument passed, else
        create a new key in self and associate the new_value argument with it.
        If length equals capacity, grow array and rehash table.
        """
        index = 0
        while index < len(self):
            if self.items[index].key == key:
                self.items[index].value = new_value
                break
            index += 1

        # If key not in self
        if index == len(self):
            # Grow if necessary and add new entry
            self.items.grow()
            self.items[index] = Entry(key, new_value)

            # Increment length
            self.length += 1

class HashDict(AbstractDict):
    """Implement dictionary using a hash table."""
    default_capacity = 13
    
    # Constructor
    def __init__(self, keys = None, values = None, capacity = None):
        """
        Instantiate self and initialize with keys and values from constructor
        arguments, if present.
        Precondition: keys and values must be iterables with same length
        Raises: ValueError
        """
        # position is used in __contains__ to remember index of item if in self
        self.position = -1
        self.max_probe_length = 0
        if capacity:
            self.capacity = capacity
        else:
            self.capacity = HashDict.default_capacity
        self.items = Array(capacity = self.capacity)
        AbstractDict.__init__(self, keys, values)

    # Accessors
    def __contains__(self, key):
        """Return True if key is in self, else return False."""
        self.position = -1
        index = abs(hash(key)) % self.items.capacity
        i = 0
        while (self.items[index + i] is not None and i < self.items.capacity):
            if self.items[index + i] != "_del_":
                if self.items[index + i].key == key:
                    self.position = index + i
                    return True
            i += 1
            
            # Wrap around to first item in array, keep i value for stop cond.
            if index + i == self.items.capacity:
                index = -i

        # Didn't find it
        return False
    
    def __getitem__(self, key):
        """
        Return the value associated with key.
        Precondition: key must be in self.
        Raises: KeyError
        """
        if not key in self:
            raise KeyError(str(key))
        else:
            # Containment search cached position of found object
            return self.items[self.position].value
        
    def __iter__(self):
        """Return an iterator on the keys in self."""
        for entry in self.items:
            if entry is not None and entry != "_del_":
                yield entry.key

    # Mutators
    def clear(self):
        """Remove every item in self and set length to 0."""
        self.items = Array(capacity = 13)
        self.length = 0

    def pop(self, key, default_value = None):
        """
        If key is in self, remove it and return the associated value, else
        return default_value.
        """
        if not key in self:
            return default_value
        else:
            # Containment search cached position of found object
            return_val = self.items[self.position].value
            # Reserved placeholder value so that __contains__ knows to keep looking after _del_
            self.items[self.position] = "_del_"
            self.length -= 1
            
        return return_val

    def rehash(self):
        """
        Copy contents of self.items into a larger array and rehash contents
        based on the new, larger capacity.
        """
        temp = HashDict(capacity = self.capacity * 2)
        for key in self:
            temp[key] = self[key]
        self.items = temp.items
        self.capacity = self.capacity * 2

    def __setitem__(self, key, new_value):
        """
        If key is in self, replace its value with the argument passed, else
        create a new key in self and associate the new_value argument with it.
        If length equals capacity, grow array and rehash table.
        """
        if key in self:
            self.items[self.position].value = new_value
        else:
            # Grow array capacity and rehash table for load factors over 0.9
            if len(self) + 1 > (0.9 * self.items.capacity):
                self.rehash()

            # Add element at available spot closest to home index
            home_index = abs(hash(key)) % self.items.capacity
            index = home_index
            new_entry = Entry(key, new_value, 0)
            i = 0
            while (self.items[index + i] is not None and
              self.items[index + i] != "_del_"):
                # Robinhood hashing!! Take from the rich (low probe length), give to the poor (high p.l.)
                # If entry at index + i has smaller probe length than that of new_entry, swap them
                # Then keep trying to find a spot for the newly evicted entry
                if new_entry.probe_length > self.items[index + i].probe_length:
                    temp = new_entry
                    new_entry = self.items[index + i]
                    self.items[index + i] = temp

                # Advance search
                i += 1
                new_entry.probe_length += 1
                
                # Wrap around
                if index + i == self.items.capacity:
                    index = -i
                    
            self.items[index + i] = new_entry
            self.max_probe_length = new_entry.probe_length
            self.length += 1
    
