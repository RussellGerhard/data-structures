from arrays import Array

"""
Author: Russell Gerhard
Implement bag ADT using an array as the underlying data structure.
"""

class ArrayBag(object):
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
        self.clear()

        if source_collection:
            for item in source_collection:
                self.add(item)

    # Accessors
    def __add__(self, other):
        """
        Return a bag that contains contents of self and other.
        Precondition: other must be of type bag.
        Raises: TypeError if other is not a bag.
        """
        # Check precondition
        if type(other) != type(self):
            raise TypeError("can only concatenate bag (not )}) to bag")
        # Create new bag
        out = ArrayBag(self)
        for item in other:
            out.add(item)
        return out

    def clone(self):
        """Return copy of self."""
        return ArrayBag(self)

    def count(self, item):
        """Return number of instances of item in self."""
        count = 0
        for obj in self:
            if obj == item:
                count += 1
        return count
    
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
            for item in self:
                if self.count(item) != other.count(item):
                    return False
            return True
        
    def is_empty(self):
        """Determine if self is empty, return True if it is, else False."""
        return (len(self) == 0)

    def __iter__(self):
        """Support iteration over the object to visit each item."""
        mod_count = self.mod_count
        
        i = 0
        while i < len(self):
            yield self.items[i]
            if mod_count != self.mod_count:
                raise RuntimeError("Cannot modify object during iteration.""")
            i += 1

    def __len__(self):
        """Return the number of items in self."""
        return self.size

    def __repr__(self):
        """Return the representation of self."""
        return str(self)

    def __str__(self):
        """Return the string representation of self."""
        return '{' + ", ".join(map(str, self)) + '}' 

    # Mutators
    def clear(self):
        """Empty self and reset size to 0."""
        self.size = 0
        self.mod_count = 0
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
        # Check precondition
        if item not in self:
            raise ValueError("ArrayBag.remove(x): x not in ArrayBag")

        # Search for index of target item
        target_index = 0
        for obj in self:
            if obj == item:
                break
            target_index += 1
            
         # Remove target item
        self.items.pop(target_index)

        # Decrement logical size and increase mod_count
        self.size -= 1
        self.mod_count += 1

class ArraySet(ArrayBag):
   def add(self, item):
        """
        Add item to self if not already in self.
        Increase size if add performed, increase capacity as needed.
        Item must be comparable, else raises ValueError.
        Precondition: self is sorted.
        Postcondition: self is sorted.
        """
        if item not in self:
            self.items.insert(len(self), item)
            self.size += 1
            self.mod_count += 1

class ArraySortedBag(ArrayBag):
    
    def add(self, item):
        """
        Add item to self in proper sorted order.
        Increase size, increase capacity as needed.
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
        if mid == 0 and len(self) == 0:
            self.items.insert(0, item)
        elif item > self.items[mid]:
            self.items.insert(mid + 1, item)
        else:
            self.items.insert(mid, item)
        self.size += 1
        self.mod_count += 1

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
                return True
        return False
            
        
                
        
if __name__ == "__main__":
    import doctest
    doctest.testmod()
