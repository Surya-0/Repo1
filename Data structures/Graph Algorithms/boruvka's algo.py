class Graph:
    def __init__(self, vertices):
        self.graph = []
        self.vertices = vertices

    def addEdge(self, u, v, w):
        self.graph.append((u, v, w))

    def find(self, parent, vertex):
        if parent[vertex] != vertex:
            parent[vertex] = self.find(parent, parent[vertex])
        return parent[vertex]

    #
    def union(self, parent, rank, vertex1, vertex2):
        parent1 = self.find(parent, vertex1)
        parent2 = self.find(parent, vertex2)
        if rank[parent1] > rank[parent2]:
            parent[parent2] = parent1
        elif rank[parent1] < rank[parent2]:
            parent[parent1] = parent2
        else:
            parent[parent2] = parent1
            rank[parent1] += 1

    def boruvkas(self):
        parent = []  # an array to store the parents of each node
        rank = []  # an array to store the ranks of each node
        num_components = self.vertices  # the number of components needs to be finally reduced to 1
        mst_weight = 0  # we calculate the weight of the mst
        for node in range(self.vertices):
            parent.append(node)
            rank.append(0)
        cheapest = [
                       -1] * self.vertices  # an array to store the vertex u,v and the weight of the shortest connecting the vertices

        while num_components > 1:
            for i in range(len(self.graph)):
                u, v, w = self.graph[i]
                set1 = self.find(parent, u)
                set2 = self.find(parent, v)

                if set1 != set2:
                    if cheapest[set1] == -1 or cheapest[set1][2] > w:
                        cheapest[set1] = [u, v, w]
                    if cheapest[set2] == -1 or cheapest[set2][2] > w:
                        cheapest[set2] = [u, v, w]

            for node in range(self.vertices):
                if cheapest[node] != -1:
                    u, v, w = cheapest[node]
                    set1 = self.find(parent, u)
                    set2 = self.find(parent, v)
                    if set1 != set2:
                        mst_weight += w
                        self.union(parent, rank, set1, set2)
                        print("Edge %d-%d with weight %d included in MST" % (u, v, w))
                        num_components -= 1

            # cheapest = [-1] * self.vertices
        print(mst_weight)


if __name__ == '__main__':
    g = Graph(4)
    g.addEdge(0, 1, 10)
    g.addEdge(0, 2, 6)
    g.addEdge(0, 3, 5)
    g.addEdge(1, 3, 15)
    g.addEdge(2, 3, 4)

    g.boruvkas()
