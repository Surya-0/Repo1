class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, vertex, edge):
        if vertex in self.graph:
            self.graph[vertex].append(edge)
        else:
            self.graph[vertex] = []
            self.graph[vertex].append(edge)

    def dfs(self, start):
        visited = [start]
        stack = [start]
        while stack:
            top = stack.pop()
            print(top)
            if top in self.graph:
                for neighbor in self.graph[top]:
                    if neighbor not in visited:
                        visited.append(neighbor)
                        stack.append(neighbor)

    def bfs(self, start):
        visited = [start]
        queue = [start]
        while queue:
            top = queue.pop(0)
            print(top)
            if top in self.graph:
                for neighbor in self.graph[top]:
                    if neighbor not in visited:
                        visited.append(neighbor)
                        queue.append(neighbor)


if __name__ == '__main__':
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
    print(graph.graph)
    print("\nThe dfs traversal is")
    graph.dfs('A')
    print("\nThe bfs traversal is")
    graph.bfs('A')
