"""

CHANGED IN VSCODE

Author:  Russell Gerhard
Purpose: Implement bag ADT using an array or linked list, implement a sorted bag
         using an array and inheriting from the array-implemented bag. Modified.

Exports:
    ArrayBag: Bag ADT implementation using an array.
    
    ArraySortedBag: Sorted bag ADT implementation using an array.
    
    LinkedBag: Bag ADT implementation using a linked list.
"""

from abstractclasses.abstractbag import AbstractBag
from dynamicarray import Array
from lists import DoublyLinkedList

class ArrayBag(AbstractBag):
    """Implement bag ADT using an array."""
    default_capacity = 10

    def __init__(self, source_collection = None):
        """Initialize self, optionally including items in source_collection."""
        self.items = Array(ArrayBag.default_capacity)
        self.position = -1
        AbstractBag.__init__(self, source_collection)
        
    # Accessors
    def __contains__(self, item):
        """
        Return True if item in self, set self.position to index.
        Else return False.
        """
        self.position = -1
        for obj in self:
            self.position += 1
            if item == obj:
                return True
        self.position = -1
        return False
    
    def __iter__(self):
        """Support iteration over self."""        
        i = 0
        while i < len(self):
            yield self.items[i]
            i += 1

    # Mutators
    def clear(self):
        """Empty self, reset length to 0 and position tracker to -1."""
        self.length = 0
        self.position = -1
        self.items = Array(ArrayBag.default_capacity)

    def add(self, item):
        """
        Add item to self, increase capacity of underlying array if necessary.
        Increment length.
        """
        # Grow underlying array if necessary
        self.items.grow()
        self.items[self.items.size()] = item
        self.length += 1

    def remove(self, item):
        """
        Remove item from self, decrement length.
        Precondition: Item is in self.
        Raises: ValueError if item is not in self.
        Postcondition: Item is not in self.
        """
        # Reset position and check precondition
        if item not in self:
            raise ValueError("ArrayBag.remove(x): x not in ArrayBag")
        
        # Remove target item
        i = self.position + 1
        while i < self.items.size():
            self.items[i - 1] = self.items[i]
            i += 1
        # i is now self.items.size()
        self.items[i - 1] = self.items.fill_value

        # Decrement logical_size and shrink if necessary
        self.items.logical_size -= 1
        self.items.shrink()

        # Decrement length
        self.length -= 1


class ArraySortedBag(ArrayBag):
    
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
        Add item to self, increase length, increase capacity as needed.
        Item must be comparable, else raises ValueError.
        Precondition: self is sorted.
        Postcondition: self is sorted.
        """

        # Check comparable item
        try:
            item < item
        except TypeError:
            msg = f"{type(self).__name__} must only contain items that support comparison."
            raise TypeError(msg)

        # Check item comparable with items in bag already
        if not self.is_empty():
            try:
                item < self.items[0]
            except TypeError:
                msg = f"{item} does not support comparison with bag element: {self.items[0]}."
                raise TypeError(msg)
        
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

        # Grow underlying array if necessary
        self.items.grow()

        # Insert in correct position
        if self.is_empty():
            insert_index = 0
        # Item larger than mid value must be inserted in front
        elif item > self.items[mid]:
            insert_index = mid + 1
        else:
            insert_index = mid

        i = self.items.size()
        while i != insert_index:
            self.items[i] = self.items[i - 1]
            i -= 1
        self.items[insert_index] = item
        self.length += 1

class LinkedBag(AbstractBag):
    """Implement bag ADT using a linked list."""

    def __init__(self, source_collection = None):
        """Initialize self, optionally including items in source_collection."""
        self.items = DoublyLinkedList()
        self.position = -1
        AbstractBag.__init__(self, source_collection)

    # Accessors
    def __contains__(self, item):
        """
        Return True if item in self, set self.position to index.
        Else return False.
        """
        self.position = -1
        probe = self.items.head
        while probe is not None:
            self.position += 1
            if item == probe.data:
                return True
            probe = probe.next
        
        self.position = -1
        return False
    
    def __iter__(self):
        """Support iteration over the object to visit each item."""
        probe = self.items.head
        while probe is not None:
            yield probe.data
            probe = probe.next

    # Mutators
    def clear(self):
        """Empty self, reset length to 0 and position tracker to -1."""
        self.length = 0
        self.position = -1
        self.items = DoublyLinkedList()

    def add(self, item):
        """Add item to self, increment length."""
        self.items.insert(len(self), item)
        self.length += 1

    def remove(self, item):
        """
        Remove item from self, decrement length.
        Precondition: Item is in self.
        Raises: ValueError if item is not in self.
        Postcondition: Item is not in self.
        """
        # Reset position and check precondition
        if item not in self:
            raise ValueError("LinkedBag.remove(x): x not in LinkedBag")
            
         # Remove target item
        self.items.pop(self.position)

        # Decrement length
        self.length -= 1