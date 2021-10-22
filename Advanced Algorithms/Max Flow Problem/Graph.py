# Ford-Fulkerson Algorithm - The simple idea
# Start with an initial flow of 0
# While there is an augmenting path from source(s):
#    Add this path-sink to flow
# Return flow

# Implementation of the Ford-Fulkerson Algorithm
from collections import defaultdict


# Representing a direct graph using adjacency matrix
class Graph:
    def __init__(self, graph):
        self.graph = graph  # residual graph
        self.row = len(graph)

    '''
    Returns if there is a path from sources 's' to sink 't' in
    residual graph. Also fills parent[] to store the path
    '''

    def BFS(self, s, t, parent):
        # Mark all vertices as not visited
        visited = [False] * self.row

        # Create a queue for BFS
        queue = []

        # Mark the source node as visited and enqueue it
        queue.append(s)
        visited[s] = True

        # Standard BFS loop
        while queue:
            # Dequeue a vertex from queue and print it
            u = queue.pop(0)

            # Get all adjacent vertices of the dequeued vertex u
            # If adjacent vertex has not been visited, then mark it
            # visited and enqueue it
            for index, value in enumerate(self.graph[u]):
                # If we find a connection to the sink node,
                # then there is no point in BFS anymore.
                # Just set its parent and return true
                if visited[index] is False and value > 0:
                    queue.append(index)
                    visited[index] = True
                    parent[index] = u
                    if index == t:
                        return True

        # We didn't reach sink in BFS starting
        # from source, so return false
        return False

    # Return the maximum flow from s to t in the given graph
    def ford_fulkerson(self, source, sink):
        # This array is filled by BFS and to store path
        parent = [-1] * self.row

        max_flow = 0  # There is no flow initially

        # Augment the flow while there is path from source to sink
        while self.BFS(source, sink, parent):
            # Find minimum residual capacity of the edges along the
            # path filled by BFS. Or find the maximum flow

            path_flow = float("Inf")  # initialize with the maximum value
            s = sink
            while s != source:
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            # Add path flow to overall flow
            max_flow += path_flow

            # Update residual capacities of the edges and reverse edges
            # along the path
            v = sink
            while v != source:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]
        return max_flow


if __name__ == '__main__':
    test_graph = [[0, 8, 9, 5, 0, 0, 0],
                  [0, 0, 0, 0, 6, 0, 0],
                  [0, 0, 0, 7, 0, 5, 0],
                  [0, 0, 0, 0, 2, 6, 0],
                  [0, 0, 0, 0, 0, 4, 11],
                  [0, 0, 0, 0, 0, 0, 13],
                  [0, 0, 0, 0, 0, 0, 0]]
    g = Graph(test_graph)
    test_source = 0
    test_sink = 6

    print("The maximum possible flow is: %d" % g.ford_fulkerson(test_source, test_sink))
