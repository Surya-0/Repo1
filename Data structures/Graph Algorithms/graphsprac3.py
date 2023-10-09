class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def bellman_ford(self, source):
        # Initialize distances to all vertices as infinite and the source as 0
        distance = [float("inf")] * self.V
        distance[source] = 0

        # Relax all edges V-1 times to find the shortest path
        for _ in range(self.V - 1):
            for u, v, w in self.graph:
                if distance[u] != float("inf") and distance[u] + w < distance[v]:
                    distance[v] = distance[u] + w

        # Check for negative weight cycles
        for u, v, w in self.graph:
            if distance[u] != float("inf") and distance[u] + w < distance[v]:
                print("Graph contains a negative weight cycle")
                return

        # Print the distances from the source vertex
        self.print_distances(distance)

    def print_distances(self, distance):
        print("Vertex Distance from Source:")
        for i in range(self.V):
            print(f"{i}: {distance[i]}")


# Example usage:
g = Graph(5)
g.add_edge(0, 1, 6)
g.add_edge(0, 3, 7)
g.add_edge(1, 2, 5)
g.add_edge(1, 3, 8)
g.add_edge(1, 4, -4)
g.add_edge(2, 1, -2)
g.add_edge(3, 2, -3)
g.add_edge(3, 4, 9)
g.add_edge(4, 0, 2)
g.add_edge(4, 2, 7)

source_vertex = 0
g.bellman_ford(source_vertex)