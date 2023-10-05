class Graph:
    def __init__(self):
        self.adList = {}

    def add_vertex(self, vertex):
        self.adList[vertex] = []

    def add_edge(self, vertex1, vertex2):
        self.adList[vertex1].append(vertex2)

    def TopologicalSort(self):
        in_degree = {v: 0 for v in self.adList}

        for vertex in self.adList:
            for adjacent_v in self.adList[vertex]:
                in_degree[adjacent_v] += 1

        queue = []
        topological_order = []
        for i in in_degree:
            if in_degree[i] == 0:
                queue.append(i)

        while queue:
            popVertex = queue.pop(0)
            topological_order.append(popVertex)

            for adjacent_v in self.adList[popVertex]:
                in_degree[adjacent_v] -= 1
                if in_degree[adjacent_v] == 0:
                    queue.append(adjacent_v)

        return topological_order


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

# graph.add_edge("A", "C")
# graph.add_edge("C", "E")
# graph.add_edge("E", "H")
# graph.add_edge("E", "F")
# graph.add_edge("F", "G")
# graph.add_edge("B", "D")
# graph.add_edge("B", "C")
# graph.add_edge("D", "F")
print(graph.adList)
print(graph.TopologicalSort())