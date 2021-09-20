from arrays import Array
from abstractbag import AbstractBag

"""
Author: Russell Gerhard
Implement bag ADT using an array as the underlying data structure.
"""

class ArrayBag(AbstractBag):
    """
    Implement bag ADT using an array.

    >>> b = ArrayBag()
    >>> b.is_empty()
    True
    >>> b.add(10)
    >>> b.is_empty()
    False
    >>> len(b)
    1
    >>> b.add('a')
    >>> len(b)
    2
    >>> b.clear()
    >>> b.is_empty()
    True
    >>> len(b)
    0
    >>> b.add(1)
    >>> b.add('a')
    >>> 1 in b
    True
    >>> 'c' in b
    False
    >>> a = ArrayBag([2,3,4])
    >>> b = a + b
    >>> 4 in b
    True
    >>> a.remove(2)
    >>> 2 in a
    False
    >>> a.count(3)
    1
    >>> c = ArrayBag([3,4])
    >>> a == c
    True
    """
    default_capacity = 10

    def __init__(self, source_collection = None):
        """Initialize self, optionally including items in source_collection."""
        self.items = Array(ArrayBag.default_capacity)
        self.position = -1
        AbstractBag.__init__(self, source_collection)

    def __contains__(self, item):
        """Return True if item in self, set self.position to index. Else return False."""
        for obj in self:
            self.position += 1
            if item == obj:
                return True
        # Did not find item
        self.position = -1
        return False
        
    # Accessors
    def __iter__(self):
        """Support iteration over the object to visit each item."""
        mod_count = self.mod_count
        
        i = 0
        while i < len(self):
            yield self.items[i]
            if mod_count != self.mod_count:
                raise RuntimeError("Cannot modify object during iteration.""")
            i += 1

    # Mutators
    def clear(self):
        """Empty self and reset size to 0."""
        self.size = 0
        self.mod_count = 0
        self.position = -1
        self.items = Array(ArrayBag.default_capacity)

    def add(self, item):
        """Add item to self, increase size of underlying array if necessary."""
        self.mod_count += 1
        self.items.insert(len(self), item)
        self.size += 1

    def remove(self, item):
        """
        Remove item from self.
        Precondition: Item is in self.
        Raises: ValueError if item is not in self.
        Postcondition: Item is not in self.
        """
        # Reset position and check precondition
        self.position = -1
        if item not in self:
            raise ValueError("ArrayBag.remove(x): x not in ArrayBag")

##        # __contains__ sets position if item in self; search loop not needed.
##        # Search for index of target item
##        target_index = self.position
##        for obj in self:
##            if obj == item:
##                break
##            target_index += 1
        
        # Remove target item
        self.items.pop(self.position)

        # Decrement logical size and increase mod_count
        self.size -= 1
        self.mod_count += 1

class ArraySortedBag(ArrayBag):
    # This is superfluous because python calls super.__init__() if __init__ is
    # missing from the subclass.
    def __init__(self, source_collection = None):
        """Initialize self, optionally including items in source_collection."""
        ArrayBag.__init__(self, source_collection)

    # Accessors
    def __contains__(self, item):
        """
        Determine if self contains item.
        Return True if so, else return False.
        """

        left = 0
        right = len(self) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if item < self.items[mid]:
                right = mid - 1
            elif item > self.items[mid]:
                left = mid + 1
            else:
                self.position = mid
                return True
            
        return False

    def __eq__(self, other):
        """
        Determine if self is equal to other.
        Return True if self and other of same type and contain same items.
        Return False else.
        """
        if self is other:
            return True
        elif type(self) != type(other):
            return False
        elif len(self) != len(other):
            return False
        else:
            for (item1, item2) in zip(self, other):
                if item1 != item2:
                    return False
        return True

    # Mutators  
    def add(self, item):
        """
        Add item to self if not already in self.
        Increase size if add performed, increase capacity as needed.
        Item must be comparable, else raises ValueError.
        Precondition: self is sorted.
        Postcondition: self is sorted.
        """
        
        # Binary search for index position
        left = 0
        right = len(self) - 1
        mid = 0
        
        while left <= right:
            mid = (left + right) // 2
            if item > self.items[mid]:
                left = mid + 1
            elif item < self.items[mid]:
                right = mid - 1
            else:
                break

        # Insert in correct position
        if self.is_empty():
            self.items.insert(0, item)
        elif item > self.items[mid]:
            self.items.insert(mid + 1, item)
        else:
            self.items.insert(mid, item)
            
        self.size += 1
        self.mod_count += 1

class ArraySet(ArrayBag):
    # This is superfluous because python calls super.__init__() if __init__ is
    # missing from the subclass.
    def __init__(self, source_collection = None):
        """Initialize self, optionally including items in source_collection."""
        ArrayBag.__init__(self, source_collection)
    
    def add(self, item):
        """
        Add item to self in proper sorted order.
        Increase size, increase capacity as needed.
        """
        if item not in self:
            self.items.insert(len(self), item)
            self.size += 1
            self.mod_count += 1

class ArraySortedSet(ArraySortedBag):
    def __init__(self, source_collection = None):
        """Initialize self, optionally including items in source_collection."""
        ArraySortedBag.__init__(self, source_collection)

    def add(self, item):
        """
        Add item to self if not already in self.
        Increase size if add performed, increase capacity as needed.
        Item must be comparable, else raises ValueError.
        Precondition: self is sorted.
        Postcondition: self is sorted.
        """
        if item not in self:
            ArraySortedBag.add(self, item)

        
if __name__ == "__main__":
    import doctest
    doctest.testmod()
