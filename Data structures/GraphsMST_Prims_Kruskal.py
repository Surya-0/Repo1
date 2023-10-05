import heapq


class Graph:
    def __init__(self):
        self.adList = {}
        self.edges = []
        self.weights = {}

    def add_vertex(self, vertex):
        self.adList[vertex] = []

    def add_edge(self, vertex1, vertex2, weight):
        self.adList[vertex1].append(vertex2)
        self.adList[vertex2].append(vertex1)
        self.weights[vertex1, vertex2] = weight
        self.weights[vertex2, vertex1] = weight

        self.edges.append((weight, vertex1, vertex2))

    def find(self, parent, vertex):
        if parent[vertex] != vertex:
            parent[vertex] = self.find(parent, parent[vertex])
        return parent[vertex]

    def union(self, rank, parent, vertex1, vertex2):
        root1 = self.find(parent, vertex1)
        root2 = self.find(parent, vertex2)
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        elif rank[root2] > rank[root1]:
            parent[root1] = root2
        else:
            parent[root2] = root1
            rank[root1] += 1

    def kruskal(self):
        mst = []
        parent = {_: _ for _ in self.adList}
        rank = {_: 0 for _ in self.adList}

        priority_queue = []
        for _ in self.edges:
            heapq.heappush(priority_queue, _)

        while priority_queue:
            weight, vertex1, vertex2 = heapq.heappop(priority_queue)

            if self.find(parent, vertex1) != self.find(parent, vertex2):
                mst.append((vertex1, vertex2, weight))
                self.union(rank, parent, vertex1, vertex2)

        return mst

    def prims(self, source):
        visited = []
        priority_queue = [(0, source, None)]
        mst = []

        while priority_queue:
            weight, popVertex, parentVertex = heapq.heappop(priority_queue)
            if popVertex not in visited:
                visited.append(popVertex)

                if parentVertex is not None:
                    mst.append((parentVertex, popVertex, weight))


                for adjacent_v in self.adList[popVertex]:
                    if adjacent_v not in visited:
                        heapq.heappush(priority_queue, (self.weights[popVertex, adjacent_v], adjacent_v, popVertex))

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

print(graph.prims('A'))
print(graph.kruskal())