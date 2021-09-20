from node import LinkedList, Node
from abstractbag import AbstractBag

"""
Author: Russell Gerhard
Implement bag ADT using a linked list as the underlying data structure.
"""

class LinkedBag(AbstractBag):
    """
    Implement bag ADT using a linked list.

    >>> b = LinkedBag()
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
    >>> a = LinkedBag([2,3,4])
    >>> b = a + b
    >>> 4 in b
    True
    >>> a.remove(2)
    >>> 2 in a
    False
    >>> a.count(3)
    1
    >>> c = LinkedBag([3,4])
    >>> a == c
    True
    """
    default_capacity = 10

    def __init__(self, source_collection = None):
        """Initialize self, optionally including items in source_collection."""
        self.items = LinkedList()
        self.position = -1
        AbstractBag.__init__(self, source_collection)

    # Accessors
    def __contains__(self, item):
        """
        Return true and set self.position to item index if item in self.
        Else return False.
        """
        self.position = -1
        for obj in self:
            self.position += 1
            if item == obj:
                return True
        return False
    
    def __iter__(self):
        """Support iteration over the object to visit each item."""
        probe = self.items.head
        while probe != None:
            yield probe.data
            probe = probe.next

    # Mutators
    def clear(self):
        """Empty self and reset size to 0."""
        self.size = 0
        self.items = LinkedList()

    def add(self, item):
        """Add item to self, increase size of underlying array if necessary."""
        self.items.insert(0, item)
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
            raise ValueError("LinkedBag.remove(x): x not in LinkedBag")
            
         # Remove target item
        self.items.pop(self.position)

        # Decrement logical size
        self.size -= 1
        self.mod_count += 1


class LinkedSortedBag(LinkedBag):
    """Implement sorted bag using a linked list."""
    def __init__(self, source_collection = None):
        """Initialize self, optionally including items from source_collection."""
        LinkedBag.__init__(self, source_collection)

    # Accessors
    def __eq__(self, other):
        """Determine if self and other are equal."""
        if self is other:
            return True
        elif type(self) != type(other):
            return False
        elif len(self) != len(other):
            return False
        else:
            other_iter = iter(other)
            for item in self:
                if item != next(other_iter):
                    return False
            return True
    
    # Mutators
    def add(self, item):
        """
        Add item to self in sorted order.
        Precondition: Item is comparable, bag is sorted.
        Raises: ValueError if item isn't comparable.
        Postcondition: Bag is sorted.
        """

        # Linear search b/c binary no faster due to O(n) access in LinkedList
        index = 0
        for obj in self:
            if obj > item:
                break
            index += 1

        self.items.insert(index, item)
        self.size += 1
        self.mod_count += 1
            

class LinkedSet(LinkedBag):

    # This is superfluous b/c Python default calls super init if no init present
    def __init__(self, source_collection = None):
        """Initialize self, optionally including items in source_collection."""
        LinkedBag.__init__(self, source_collection)

    
    def add(self, item):
        """
        Add item to self if not already in self.
        Increase size if add performed, increase capacity as needed.
        """
        if item not in self:
            self.items.insert(0, item)
            self.size += 1

class LinkedSortedSet(LinkedSortedBag):
    def __init__(self, source_collection = None):
        """Initialize self, optionally including items in source_collection."""
        LinkedSortedBag.__init__(self, source_collection)

    def add(self, item):
        """Add item to self in sorted order if not already in self."""
        if item not in self:
            LinkedSortedBag.add(self, item)
        
        
if __name__ == "__main__":
    import doctest
    doctest.testmod()
