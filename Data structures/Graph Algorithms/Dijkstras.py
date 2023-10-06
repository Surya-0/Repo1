import heapq
class Graph:
    def __init__(self):
        self.adList = {}
        self.weights = {}

    def add_vertex(self, vertex):
        self.adList[vertex] = []

    def add_edge(self, vertex1, vertex2, weight):
        self.adList[vertex1].append(vertex2)
        self.weights[(vertex1, vertex2)] = weight

    def dijkstras(self, source):
        distances = {}
        for vertex in self.adList:
            distances[vertex] = float('inf')

        distances[source] = 0
        priority_queue = [(0, source)]
        while priority_queue:
            popDistance, popVertex = heapq.heappop(priority_queue)
            for adjacent_v in self.adList[popVertex]:
                new_dist = distances[popVertex] + self.weights[(popVertex, adjacent_v)]

                if new_dist < distances[adjacent_v]:
                    distances[adjacent_v] = new_dist
                    heapq.heappush(priority_queue, (new_dist, adjacent_v))

        return distances



graph=Graph()
graph.add_vertex('A')
graph.add_vertex('B')
graph.add_vertex('C')
graph.add_vertex('D')
graph.add_vertex('E')
# graph.add_vertex('F')
# graph.add_vertex('G')
# graph.add_vertex('H')
# graph.add_vertex('I')
# graph.add_vertex('J')

graph.add_edge('A', 'B', 4)
graph.add_edge('A', 'C', 1)
graph.add_edge('C', 'D', 4)
graph.add_edge('C', 'B', 2)
graph.add_edge('B', 'E', 4)
graph.add_edge('D', 'E', 4)

# graph.add_edge('D', 'G', 1)
# graph.add_edge('G', 'H', 2)
# graph.add_edge('F', 'J', 1)
# graph.add_edge('J', 'I', 2)
print(graph.adList)
print(graph.dijkstras('A'))