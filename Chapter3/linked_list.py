"""This module implements a basic linked list data structure."""

class Node():
    """One element in a linked list."""

    def __init__(self, value, next_node):
        """
        Initialize one element in a linked list.

        Args:
            value (any): The value stored within this item of the list.
            next_node (Node): The next node in the list.
        """
        self.value = value
        self.next_node = next_node

    def get_value(self):
        """Retrieve value attribute."""
        return self.value

    def get_next_node(self):
        """Retrieve next_node attribute."""
        return self.next_node

    def set_value(self, new_value):
        """Set the value attribute of the Node."""
        self.value = new_value

    def set_next_node(self, new_next_node):
        """Set the next_node attribute of the Node."""
        self.next_node = new_next_node

class LinkedList():
    """A basic linked list implementation."""

    def __init__(self, iterable = []):
        """
        Initialize a linked list given an optional iterable.

        Args:
            iterable (Iterable): Any iterable collection.
        """
        if iterable == []:
            self.head = None
        elif len(iterable) == 1:
            self.head = Node(iterable[0], None)
        else:
            n = len(iterable)
            last_node = Node(iterable[n - 1], None)
            for i in range(n - 2, -1, -1):
                if i == 0:
                    self.head = Node(iterable[i], last_node)
                else:
                    node = Node(iterable[i], last_node)
                    last_node = node

    def get_head(self):
        return self.head

    def prepend(self, value):
        node = Node(value, self.head)
        self.head = node

    def append(self, value):
        current = self.get_head()
        while current.get_next_node() != None:
            current = current.get_next_node()
        node = Node(value, None)
        current.set_next_node(node)

    def insert(self, index, value):
        current = self.head
        index -= 1
        while index > 0:
            current = current.get_next_node()
            index -= 1
        node = Node(value, current.get_next_node())
        current.set_next_node(node)

    def __str__(self):
        out = "["
        current = self.get_head()
        while current.get_next_node() != None:
            out += f"{current.get_value()}, "
            current = current.get_next_node()
        out += f"{current.get_value()}]"
        return out

    def __repr__(self):
        out = "["
        current = self.get_head()
        while current.get_next_node() != None:
            out += f"{current.get_value()}, "
            current = current.get_next_node()
        out += f"{current.get_value()}]"
        return out
        
        

    
