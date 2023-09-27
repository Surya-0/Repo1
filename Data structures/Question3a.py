# Let G be a connected weighted undirected graph with distinct edge weights. Prove that the following algorithm finds
# an MST of G. “Initially all the edges are unmarked. Let e be an unmarked edge with the highest weight. If removing e
# does not disconnect the graph, remove it; otherwise, mark it. Repeat this process until the graph consists of
# marked edges only. Then, output the current graph as an MST of the original graph.”Also, submit the algorithm and
# time complexity.

def sorting_key(x):
    return x[1]


class Graph:
    def __init__(self):
        self.adjacency_list = {}  # undirected graph
        self.edges = {}
        self.no_connected_vertices = 0
        self.marked_edges = []

    def add_vertex(self, vertex):
        self.adjacency_list[vertex] = []  # initialising vertices with no edges

    def add_edge(self, source, destination, weight):
        self.adjacency_list[source].append(destination)
        self.adjacency_list[destination].append(source)
        self.edges[(source, destination)] = weight
        self.edges[(destination, source)] = weight

    def DFS(self, source):
        connected_no = 0
        visited = [source]
        stack = [source]
        while stack:
            pop_vertex = stack.pop(0)
            connected_no += 1
            for neighbours in self.adjacency_list[pop_vertex]:
                if neighbours not in visited:
                    visited.append(neighbours)
                    stack.append(neighbours)
        return connected_no

    def mst(self, source):
        sorted_edges = list(self.edges.items())
        sorted_edges.sort(key=sorting_key, reverse=True)
        print(sorted_edges)

        while sorted_edges:
            edge = sorted_edges.pop(0)
            source, destination = edge[0]
            weight = edge[1]
            self.adjacency_list[source].remove(destination)
            connected = self.DFS(source)
            if connected != self.no_connected_vertices:
                self.marked_edges.append(edge)
                self.adjacency_list[source].append(destination)


graph = Graph()
vertices = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
edges = [('A', 'B', 2), ('A', 'C', 3), ('A', 'D', 5), ('B', 'D', 7), ('B', 'E', 9), ('C', 'D', 6),
         ('C', 'F', 8), ('D', 'E', 4), ('D', 'F', 6), ('D', 'G', 4), ('E', 'G', 1), ('F', 'G', 8)]

for vertex in vertices:
    graph.add_vertex(vertex)

for edge in edges:
    graph.add_edge(edge[0], edge[1], edge[2])

print(graph.adjacency_list)
graph.no_connected_vertices = graph.DFS('A')
print(graph.no_connected_vertices)
graph.mst('A')
print(graph.marked_edges)