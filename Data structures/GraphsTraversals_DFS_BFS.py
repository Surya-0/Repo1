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

    def bfs(self, source):
        visited = [source]
        queue = [source]
        while queue:
            popVertex = queue.pop(0)
            print(popVertex)
            for adjacent_v in self.adList[popVertex]:
                if adjacent_v not in visited:
                    queue.append(adjacent_v)
                    visited.append(adjacent_v)

    def dfs(self, source):
        visited = [source]
        stack = [source]
        while stack:
            popVertex = stack.pop()
            print(popVertex)
            for adjacent_v in self.adList[popVertex]:
                if adjacent_v not in visited:
                    stack.append(adjacent_v)
                    visited.append(adjacent_v)

    def djikstras(self, source):
        distance = {v: float('inf') for v in self.adList}
        distance[source] = 0
        priority_queue = [(0, source)]

        while priority_queue:
            weight, popVertex = heapq.heappop(priority_queue)
            for adjacent_v in self.adList[popVertex]:
                new_dist = weight + self.weights[popVertex, adjacent_v]
                if new_dist < distance[adjacent_v]:
                    distance[adjacent_v] = new_dist
                    heapq.heappush(priority_queue, (new_dist, adjacent_v))

        return distance


    def topologicalsort(self):
        in_degree = {v: 0 for v in self.adList}
        for vertex in self.adList:
            for adjacent_v in self.adList[vertex]:
                in_degree[adjacent_v] += 1
        queue = []
        topological_sort_array = []
        for vertex in in_degree:
            if in_degree[vertex] == 0:
                queue.append(vertex)

        while queue:
            popVertex = queue.pop(0)
            topological_sort_array.append(popVertex)
            for adjacent_v in self.adList[popVertex]:
                in_degree[adjacent_v] -= 1
                if in_degree[adjacent_v] == 0:
                    queue.append(adjacent_v)
        return topological_sort_array


graph=Graph()
graph.add_vertex('A')
graph.add_vertex('B')
graph.add_vertex('C')
graph.add_vertex('D')
graph.add_vertex('E')

graph.add_edge('A', 'B', 4)
graph.add_edge('A', 'C', 1)
graph.add_edge('C', 'D', 4)
graph.add_edge('C', 'B', 2)
graph.add_edge('B', 'E', 4)
graph.add_edge('D', 'E', 4)

print(graph.adList)
print()
# graph.bfs('A')
# print()
# graph.dfs('A')
# print(graph.topologicalsort())
# print(graph.djikstras('A'))