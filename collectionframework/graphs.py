"""
Author:  Russell Gerhard
Purpose: Implement different types of graphs (weighted/unweighted, directed/
         undirected) using either an adjacency list or an adjacency matrix.

Exports:
    Vertex: Graph vertex object that contains a label and a linked edge list.

    ALDirectedGraph: Directed graph that supports edge weights, implemented using
                     an adjacency list.
    
    ALUndirectedGraph: Undirected graph that supports edge weights, implemented
                       using an adjacency list.
"""

from dicts import HashDict
from lists import LinkedAdjacencyList

class Vertex():
    """Represent a vertex in a graph."""
    def __init__(self, label):
        """Initialize vertex with label, edge list is linked list."""
        self.label = label
        self.edge_list = LinkedAdjacencyList()

    # Accessors
    def __eq__(self, other):
        """Determine if two vertices are equal."""
        if self is other:
            return True
        elif type(self) != type(other):
            return False
        else:
            if self.label == other.label:
                return True
            else:
                return False

    def incident_edges(self):
        """Return an iterator over the incident edges of the vertex."""
        return edge_list.iter_node()

    def neighbors(self):
        """Return an iterator over all neighboring vertices of the vertex."""
        return iter(self.edge_list)

    def __repr__(self):
        """Return unique string representation of self."""
        return str(self)

    def __str__(self):
        """Return string representation of self."""
        out = f"Vertex({self.label}, "
        out += str(self.edge_list)
        out += ')'
        return out

    # Mutators
    def add_edge(self, neighbor, weight = 1):
        """Add an edge to the edge list of self."""
        self.edge_list.add(neighbor, weight)

    def del_edge(self, neighbor):
        """
        Remove an edge from the edge list of self.
        Precondition: edge must be in edge list.
        Raises: ValueError
        """
        if neighbor not in self.edge_list:
            raise ValueError(f"No edge from {self.label} to {neighbor}")

        self.edge_list.remove(neighbor)

class ALDirectedGraph:
    """
    Represent a directed graph with optional edge weights using adjacency
    lists.
    """
    def __init__(self, vertices = None, edges = None):
        """
        Insantiate and optionally initialize self using a collection of vertex
        names and a collection of edges between vertices listed in the vertices
        argument, with optional weights in (from, to, weight) format.
        Precondition: All edges in edges argument are incident on valid vertices.
        Raises: ValueError

        O(N + M)
        """
        self.vertices = HashDict()
        self.num_edges = 0
        self.num_vertices = 0

        # Initialize edges
        if vertices:
            for vertex in vertices:
                self.add_vertex(vertex)

        if edges:
            for edge in edges:
                if edge[0] not in self:
                    raise ValueError(f"{edge[0]} not in self.")
                elif edge[1] not in self:
                    raise ValueError(f"{edge[1]} not in self.")
                try:
                    self.add_edge(edge[0], edge[1], edge[2])
                except IndexError:
                    self.add_edge(edge[0], edge[1])
                    
    # Accessors
    def is_empty(self):
        """Return True if self has no vertices, else False."""
        if self.num_vertices == 0:
            return True
        else:
            return False

    def contians_vertex(self, vertex):
        """
        Return True if self contains vertex, else return False.
        
        O(1)
        """
        return vertex in self.vertices

    def contains_edge(self, origin, neighbor):
        """
        Return True if self contains edge between origin and neighbor, else False.
        Precondition: Origin and neighbor must be in self.
        Raises: ValueError
        
        O(M/N) avg, which is deg(vertex)
        """
        if origin not in self:
            raise ValueError(f"{origin} not in self.")
        elif neighbor not in self:
            raise ValueError(f"{neighbor} not in self.")
        
        return neighbor in self.vertices[origin].edge_list

    def get_vertex(self, label):
        """
        Get vertex corresponding label.
        Precondition: Vertex must be in self.
        Raises: ValueError
        """
        if label not in self.vertices:
            raise ValueError(f"{label} not in self.")
        
        return self.vertices[label]

    def incident_edges(self, vertex):
        """
        Return an iterator over the incident edges of the vertex.
        Precondition: vertex must be in self.
        Raises: ValueError
        
        O(M/N) avg, which is deg(vertex)
        """
        if vertex not in self:
            raise ValueError(f"{vertex} not in self.")
        
        return self.vertices[vertex].incident_edges()

    def __iter__(self):
        """
        Return an iterator over all vertices in self.

        O(N)
        """
        for key in self.vertices.keys():
            yield key
    
    def neighbors(self, vertex):
        """
        Return an iterator over the neighboring vertices of the vertex.
        Precondition: vertex must be in self.
        Raises: ValueError
        
        O(M/N) avg, which is deg(vertex)
        """
        if vertex not in self:
            raise ValueError(f"{vertex} not in self.")
        
        return self.vertices[vertex].neighbors()
    
    def get_num_edges(self):
        """Return the number of edges in self."""
        return self.num_edges

    def get_num_vertices(self):
        """Return the number of vertices in self."""
        return self.num_vertices

    def __repr__(self):
        """Return unique string representation of self."""
        out = "ALDirectedGraph("
        out += ", ".join(map(str, self.vertices.values()))
        out += ')'
        return out

    def __str__(self):
        """Return a string representation of self."""
        out = "Graph:\n"
        for value in self.vertices.values():
            out += f"{value}\n"
        if self.num_vertices > 0:
            out = out[:-1]
        return out

    # Mutators
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
        if origin not in self:
            raise ValueError(f"{origin} not in self.")
        elif neighbor not in self:
            raise ValueError(f"{neighbor} not in self.")
        elif neighbor in self.vertices[origin].edge_list:
            raise ValueError("Edge already exists in self.")
        if weight < 0:
            raise ValueError("Edge weight cannot be negative.")
        
        self.vertices[origin].add_edge(neighbor, weight)
        self.num_edges += 1
    
    def add_vertex(self, vertex_label):
        """
        Add a labeled vertex to the graph.
        Precondition: this vertex must not already exist in self.
        Raises: ValueError

        O(1)
        """
        if vertex_label in self:
            raise ValueError(f"{vertex_label} is already in self.")
        
        self.vertices[vertex_label] = Vertex(vertex_label)
        self.num_vertices += 1

    def clear(self):
        """
        Remove all vertices and edges from self.
        """
        self.vertices = HashDict()
        self.num_edges = 0
        self.num_vertices = 0

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
        if origin not in self:
            raise ValueError(f"{origin} not in self.")
        elif neighbor not in self:
            raise ValueError(f"{neighbor} not in self.")
        elif neighbor not in self.vertices[origin].edge_list:
            raise ValueError("Edge is not in self.")

        self.vertices[origin].del_edge(neighbor)
        self.num_edges -= 1

    def del_vertex(self, vertex):
        """
        Remove all edges indicent on the vertex.
        Remove the vertex itself.
        Precondition: vertex must be in self.
        Raises: ValueError

        O(M) avg, worst degrades to O(N^2)
        """
        if vertex not in self:
            raise ValueError(f"{vertex} is not in self.")
        
        for potential_neighbor in self.vertices:
            try:
                self.del_edge(potential_neighbor, vertex)
            except:
                pass
                
        self.vertices.pop(vertex)
        self.num_vertices -= 1

class ALUndirectedGraph(ALDirectedGraph):

    # Accessors
    def __repr__(self):
        """Return unique string representation of self."""
        out = "ALUndirectedGraph("
        out += ", ".join(map(str, self.vertices.values()))
        out += ')'
        return out

    # Mutators
    def add_edge(self, origin, neighbor, weight = 1):
        """
        Add an edge from origin to neighbor with weight value in origin's adjacency
        list. Also add the reverse edge with same weight from neighbor to origin.
        Precondition: origin and neighbor must be in self.
        Raises: ValueError
        Precondition: edges must not already exist in self.
        Raises: ValueError
        Precondition: weight must be nonnegative.
        Raises: ValueError

        O(1)
        """
        if origin not in self:
            raise ValueError(f"{origin} not in self.")
        elif neighbor not in self:
            raise ValueError(f"{neighbor} not in self.")
        elif neighbor in self.vertices[origin].edge_list or \
             origin in self.vertices[neighbor].edge_list:
            raise ValueError("Edge already exists in self.")
        if weight < 0:
            raise ValueError("Edge weight cannot be negative.")
        
        self.vertices[origin].add_edge(neighbor, weight)
        self.vertices[neighbor].add_edge(origin, weight)
        self.num_edges += 1

    def del_edge(self, origin, neighbor):
        """
        Remove the edge from origin to neighbor from self.
        Remove the edge from neighbor to origin from self.
        Precondition: origin and neighbor must be in self.
        Raises: ValueError
        Precondition: edges must be in self.
        Raises: ValueError

        O(M/N) avg, which is deg(vertex)
        If edge list was a BST we could get log(M/N)
        """
        if origin not in self:
            raise ValueError(f"{origin} not in self.")
        elif neighbor not in self:
            raise ValueError(f"{neighbor} not in self.")
        elif neighbor not in self.vertices[origin].edge_list or \
             origin not in self.vertices[neighbor].edge_list:
            raise ValueError("Edge is not in self.")

        self.vertices[origin].del_edge(neighbor)
        self.vertices[neighbor].del_edge(origin)
        self.num_edges -= 1
    
