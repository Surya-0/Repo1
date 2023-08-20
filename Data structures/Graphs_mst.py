import heapq


class Graph:
    def __init__(self):
        self.graph = {}
        self.weights = {}
        self.edges = []

    def add_vertex(self, vertex):
        self.graph[vertex] = []

    def add_edge(self, vertex1, vertex2, weight):
        self.graph[vertex1].append(vertex2)
        self.graph[vertex2].append(vertex1)

        self.weights[(vertex1, vertex2)] = weight
        self.weights[(vertex2, vertex1)] = weight

        self.edges.append((weight, vertex1, vertex2))

    def print_graph(self):
        for vertex in self.graph:
            print("Vertex ", vertex, " : ", self.graph[vertex])

    def prims_algo(self, source):
        visited = []
        priority_queue = [(0, source, None)]
        mst = []

        while priority_queue:
            weight, curr_vertex, parent_vertex = heapq.heappop(priority_queue)
            if curr_vertex not in visited:
                visited.append(curr_vertex)

                if parent_vertex is not None:
                    mst.append((parent_vertex, curr_vertex, weight))

                for adj_vertex in self.graph[curr_vertex]:
                    if adj_vertex not in visited:
                        heapq.heappush(priority_queue,
                                       (self.weights[(curr_vertex, adj_vertex)], adj_vertex, curr_vertex))

        return mst


graph = Graph()
graph.add_vertex('A')
graph.add_vertex('B')
graph.add_vertex('C')
graph.add_vertex('D')
graph.add_vertex('E')
graph.add_vertex('F')

graph.add_edge('A', 'B', 7)
graph.add_edge('A', 'C', 8)
graph.add_edge('C', 'D', 4)
graph.add_edge('C', 'B', 3)
graph.add_edge('C', 'E', 3)
graph.add_edge('B', 'D', 6)
graph.add_edge('D', 'E', 2)
graph.add_edge('D', 'F', 5)
graph.add_edge('E', 'F', 2)

print(graph.prims_algo('A'))
graph.print_graph()
