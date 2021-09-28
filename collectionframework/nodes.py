"""
Author:  Russell Gerhard
Purpose: Provide basic nodes for linked structures.

Exports:
    Node:       Node with data and a single node link.
    
    TwoWayNode: Node with data and two node links.
"""

class Node:
    """Represent a singly-linked node."""
    def __init__(self, data, _next = None):
        """Instantiate a node."""
        self.data = data
        self.next = _next
        
    def __str__(self):
        return f"{self.data}"

    def __repr__(self):
        return f"Node({self.data})"


class TwoWayNode(Node):
    """Represent a doubly-linked node."""
    def __init__(self, data, _next = None, prev = None):
        Node.__init__(self, data, _next)
        self.prev = prev
    
