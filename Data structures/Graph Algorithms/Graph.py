class Graph:
    def __init__(self):
        self.adList = {}

    def add_edge(self, vertex, edge):
        if vertex in self.adList:
            self.adList[vertex].append(edge)
        else:
            self.adList[vertex] = []
            self.adList[vertex].append(edge)

    def dfs(self, vertex):
        visited = [vertex]
        stack = [vertex]
        while stack:
            popVertex = stack.pop()
            print(popVertex)
            if popVertex in self.adList:
                for adjacentVertex in self.adList[popVertex]:
                    if adjacentVertex not in visited:
                        visited.append(adjacentVertex)
                        stack.append(adjacentVertex)

    def bfs(self, vertex):
        visited = [vertex]
        queue = [vertex]
        while queue:
            popVertex = queue.pop(0)
            print(popVertex)
            if popVertex in self.adList:
                for adjacentVertex in self.adList[popVertex]:
                    if adjacentVertex not in visited:
                        visited.append(adjacentVertex)
                        queue.append(adjacentVertex)


graph = Graph()
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
graph.dfs('A')
print()
graph.bfs('A')
