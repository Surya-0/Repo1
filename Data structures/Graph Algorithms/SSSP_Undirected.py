class Graph:
    def __init__(self):
        self.adList = {}

    def add_vertex(self, vertex):
        self.adList[vertex] = []

    def add_edge(self, vertex1, vertex2):
        self.adList[vertex1].append(vertex2)

    def sssp_undirected(self, source):
        direction = {}
        for vertex in self.adList:
            direction[vertex] = float('inf')

        direction[source] = 0
        queue = [source]

        while queue:
            popVertex = queue.pop(0)
            for adjacent_vertex in self.adList[popVertex]:
                if direction[adjacent_vertex] == float('inf'):
                    direction[adjacent_vertex] = direction[popVertex] + 1
                    queue.append(adjacent_vertex)

        return direction


graph=Graph()
graph.add_vertex('A')
graph.add_vertex('B')
graph.add_vertex('C')
graph.add_vertex('D')
graph.add_vertex('E')
graph.add_vertex('F')
graph.add_vertex('G')
graph.add_vertex('H')
graph.add_vertex('I')
graph.add_vertex('J')

graph.add_edge('A', 'B')
graph.add_edge('B', 'C')
graph.add_edge('C', 'D')
graph.add_edge('C', 'E')
graph.add_edge('D', 'E')
graph.add_edge('D', 'F')
graph.add_edge('D', 'G')
graph.add_edge('G', 'H')
graph.add_edge('F', 'J')
graph.add_edge('J', 'I')
print(graph.adList)
print(graph.sssp_undirected('A'))