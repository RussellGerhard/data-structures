"""
Author:  Russell Gerhard
Purpose: Provide basic nodes for linked structures.

Exports:
    BSTNode: Node used in a binary search tree.

    LinkedEdge: Node used to represent an edge with optional weight in an
                adjacency list.
    
    Node: Node with data and a single node link.
    
    TwoWayNode: Node with data and two node links (next and previous).
"""

class BSTNode:
    """Represent nodes in a binary search tree."""
    def __init__(self, data, left = None, right = None):
        """Instantiate and initialize self."""
        self.data = data
        self.left = left
        self.right = right


class Node:
    """Represent a singly-linked node."""
    def __init__(self, data, _next = None):
        """Instantiate a node."""
        self.data = data
        self.next = _next

    def __repr__(self):
        return f"Node({self.data})"
        
    def __str__(self):
        return f"{self.data}"


class LinkedEdge(Node):
    """Represent vertices in an adjacency list for a graph representation."""
    def __init__(self, data, weight = 1, _next = None):
        """Instantiate and initialize self."""
        Node.__init__(self, data, _next)
        self.weight = weight

    def __repr__(self):
        return f"ALNode({self.data}, {self.weight})"

    def __str__(self):
        return f"({self.data}, {self.weight})"


class TwoWayNode(Node):
    """Represent a doubly-linked node."""
    def __init__(self, data, _next = None, prev = None):
        Node.__init__(self, data, _next)
        self.prev = prev
        
