from linkedlist import LinkedList

## THIS IS A LEARNING FILE NOT INTENDED FOR EXPORT ##
## THIS FILE WILL NOT WORK WITHOUT A COPY OF linkedbag.py IN LOCAL DIRECTORY ##

"""
Author:  Russell Gerhard
Purpose: Implement bag ADT, without inheritance, using a linked list
         as the underlying data structure.
"""

class LinkedBag(object):
    """Implement bag ADT using a linked list."""
    default_capacity = 10

    def __init__(self, source_collection = None):
        """Initialize self, optionally including items in source_collection."""
        self.size = 0
        self.items = LinkedList()

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
        out = LinkedBag(self)
        for item in other:
            out.add(item)
        return out

    def clone(self):
        """Return copy of self."""
        return LinkedBag(self)

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
        probe = self.items.head
        while probe != None:
            yield probe.data
            probe = probe.next

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
        self.items = LinkedList()

    def add(self, item):
        """Add item to self."""
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
        self.items.remove(item)

        # Decrement logical size
        self.size -= 1

class LinkedSet(LinkedBag):
   def add(self, item):
        """
        Add item to self if not already in self.
        Increase size if add performed, increase capacity as needed.
        """
        if item not in self:
            self.items.insert(0, item)
            self.size += 1
