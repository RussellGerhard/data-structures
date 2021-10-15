"""
Author:  Russell Gerhard
Purpose: Document methods for any class implementing the directed graph ADT or
         the undirected graph ADT.
"""

class DirectedGraphInterface:
    """Specify interface for classes implementing a directed graph."""

    # Constructor
    def __init__(self, vertices = None, edges = None):
        """
        Insantiate and optionally initialize self using a collection of vertex
        names and a collection of edges between vertices listed in the vertices
        argument, with optional weights in (from, to, weight) format.
        Precondition: All edges in edges argument are incident on valid vertices.
        Raises: ValueError

        O(N + M)
        """
        pass

    # Accessors
    def is_empty(self):
        """Return True if self has no vertices, else False."""
        return True

    def contians_vertex(self, vertex):
        """
        Return True if self contains vertex, else return False.
        
        O(1)
        """
        return True

    def contains_edge(self, origin, neighbor):
        """
        Return True if self contains edge between origin and neighbor, else False.
        Precondition: Origin and neighbor must be in self.
        Raises: ValueError
        
        O(M/N) avg, which is deg(vertex)
        """
        return True

    def get_vertex(self, label):
        """
        Get vertex corresponding label.
        Precondition: Vertex must be in self.
        Raises: ValueError
        """
        return None

    def incident_edges(self, vertex):
        """
        Return an iterator over the incident edges of the vertex.
        Precondition: vertex must be in self.
        Raises: ValueError
        
        O(M/N) avg, which is deg(vertex)
        """
        return None

    def __iter__(self):
        """
        Return an iterator over all vertices in self.

        O(N)
        """
        return None
    
    def neighboring_vertices(self, vertex):
        """
        Return an iterator over the neighboring vertices of the vertex.
        Precondition: vertex must be in self.
        Raises: ValueError
        
        O(M/N) avg, which is deg(vertex)
        """
        return None

    def get_num_edges(self):
        """Return the number of edges in self."""
        return 0

    def get_num_vertices(self):
        """Return the number of vertices in self."""
        return 0

    def __repr__(self):
        """Return unique string representation of self."""
        return ''

    def __str__(self):
        """Return a string representation of self."""
        return ''

    #Mutators
    def add_edge(self, origin, neighbor, weight = 1):
        """
        Add an edge from origin to neighbor with weight value in origin's adjacency
        list.
        Precondition: origin and neighbor must be in self.
        Raises: ValueError
        Precondition: edge must not already exist in self.
        Raises: ValueError
        Precondition: weight must be nonnegative.
        Raises: ValueError

        O(1)
        """
        pass

    def add_vertex(self, vertex):
        """
        Add a vertex to the self.
        Precondition: vertex must not already exist in self.
        Raises: ValueError

        O(1)
        """
        pass

    def clear(self):
        """
        Remove all vertices and edges from the self.
        """
        pass

    def del_edge(self, origin, neighbor):
        """
        Remove the edge from origin to neighbor from self.
        Precondition: origin and neighbor must be in self.
        Raises: ValueError
        Precondition: edge must be in self.
        Raises: ValueError

        O(M/N) avg, which is deg(vertex)
        If edge list was a BST we could get log(M/N)
        """

    def del_vertex(self, vertex):
        """
        Remove all edges indicent on the vertex.
        Remove the vertex itself.
        Precondition: vertex must be in self.
        Raises: ValueError

        O(M) avg, worst degrades to O(N^2)
        """
