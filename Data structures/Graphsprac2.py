class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        self.graph[vertex] = []

    def add_edge(self, vertex1, vertex2):
        self.graph[vertex1].append(vertex2)

    def print_graph(self):
        for vertex in self.graph:
            print("Vertex ", vertex, " : ", self.graph[vertex])

    def dfs(self, vertex):
        visited = [vertex]
        stack = [vertex]
        while stack:
            top = stack.pop()
            print(top)
            for adj_element in self.graph[top]:
                if adj_element not in visited:
                    visited.append(adj_element)
                    stack.append(adj_element)

    def bfs(self, vertex):
        visited = [vertex]
        queue = [vertex]
        while queue:
            element = queue.pop(0)
            print(element)
            for adj_element in self.graph[element]:
                if adj_element not in visited:
                    visited.append(adj_element)
                    queue.append(adj_element)

    def topological_sort(self):
        in_degree = {}
        for vertex in self.graph:
            in_degree[vertex] = 0

        for vertex1 in self.graph:
            for vertex2 in self.graph[vertex1]:
                in_degree[vertex2] += 1

        print(in_degree)
        queue = []
        topological_sort = []
        for vertex in in_degree:
            if in_degree[vertex] == 0:
                queue.append(vertex)
        while queue:
            element = queue.pop(0)
            topological_sort.append(element)

            for vertex in self.graph[element]:
                in_degree[vertex] -= 1
                if in_degree[vertex] == 0:
                    queue.append(vertex)

        if len(topological_sort) != len(self.graph):
            print("Graph contains a cycle")
            return
        return topological_sort


graph = Graph()
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

graph.print_graph()
print("DFS traversal : ")
graph.dfs('A')
print(" ")
print("BFS traversal : ")
graph.bfs('A')
print(graph.topological_sort())