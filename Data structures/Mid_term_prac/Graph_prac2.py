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
        self.weights[(vertex1, vertex2)] = weight
        self.weights[(vertex2, vertex1)] = weight
        self.edges.append((weight, vertex1, vertex2))

    def find(self, parent, vertex):
        if parent[vertex] != vertex:
            parent[vertex] = self.find(parent, parent[vertex])
        return parent[vertex]

    def union(self, rank, parent, vertex1, vertex2):
        root1 = self.find(parent,vertex1)
        root2 = self.find(parent,vertex2)
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        elif rank[root1] < rank[root2]:
            parent[root1] = root2
        else:
            parent[root2] = root1
            rank[root1] += 1

    def kruskal(self):
        mst = []
        parent = {}
        rank = {}
        for i in self.adList:
            parent[i] = i
            rank[i] = i
        priority_queue = []
        for i in self.edges:
            heapq.heappush(priority_queue, i)

        while priority_queue:
            weight, vertex1, vertex2 = heapq.heappop(priority_queue)
            if self.find(parent, vertex1) != self.find(parent, vertex2):
                mst.append((vertex1, vertex2, weight))
                self.union(rank, parent, vertex1, vertex2)
        print(mst)

    def prims(self,source):
        visited = []
        priority_queue = [(0,source,None)]
        mst = []

        while priority_queue:
            weight,child_vertex, parent_vertex = heapq.heappop(priority_queue)
            if child_vertex not in visited:
                visited.append(child_vertex)

                if parent_vertex is not None:
                    mst.append((parent_vertex, child_vertex,weight))

                for adjacent_vertex in self.adList[child_vertex]:
                    if adjacent_vertex not in visited:
                        heapq.heappush(priority_queue,(self.weights[(adjacent_vertex,child_vertex)],adjacent_vertex,child_vertex))

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
graph.kruskal()