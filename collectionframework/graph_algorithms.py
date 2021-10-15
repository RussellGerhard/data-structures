"""
Author:  Russell Gerhard
Prupose: Implement common graph processing algorithms for different types of
         graphs.

Exports:

"""

from graphs import ALDirectedGraph, ALUndirectedGraph
from stacks import DoublyLinkedStack
from queues import DoublyLinkedQueue

def bfs(graph, s: int):
    """
    Generate and return BFS tree using vertex s as a starting point.
    Expects an adjacency list, works for directed and undirected.

    O(N + M) because each node is enqueued and dequeued once, and
    scanning each adjacency list to check for visitedness results
    in scanning all edges in the graph.

    Note: bfs is O(N^2) with an adjacency matrix.
    """
    # Intialize array to track whether vertices have been visited
    visited = [False] * graph.get_num_vertices()
    visited[s] = True

    # Initialize queue to schedule vertices to be visited
    vertex_queue = DoublyLinkedQueue()
    vertex_queue.add(s)

    # Initialize output graph (tree)
    bfs_tree = type(graph)()
    bfs_tree.add_vertex(s)
    
    # Perform search
    while not vertex_queue.is_empty():
        vertex_label = vertex_queue.pop()
        vertex = graph.get_vertex(vertex_label)
        for neighbor_label in vertex.neighbors():
            if not visited[neighbor_label]:
                visited[neighbor_label] = True
                vertex_queue.add(neighbor_label)
                bfs_tree.add_vertex(neighbor_label)
                bfs_tree.add_edge(vertex_label, neighbor_label)

    # To tell if connected, compare sum of visited to num_vertices         
    print(f"Connected: {sum(visited) == graph.get_num_vertices()}")

    # To tell if path exists from s to t, start bfs at s and check
    # if t ends up in bfs_tree
    print(f"0 reachable from {s}: {0 in bfs_tree}")

    # To get a forest for disconnected graph, start new bfs searches
    # from any node unvisited while there still are unvisited nodes

    return bfs_tree
    
