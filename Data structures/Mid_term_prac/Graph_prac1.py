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
    g = Graph()
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(3, 1)
    g.add_edge(2, 4)
    g.add_edge(4, 5)
    g.add_edge(5, 6)
    g.add_edge(6, 4)
    print(g.graph)
    print("\nThe dfs traversal is")
    g.dfs(1)
    print("\nThe bfs traversal is")
    g.bfs(1)
