class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = {}
        self.reverse_graph = {}

    def dfs(self, arr, vertex):
        visited = [vertex]
        stack = [vertex]
        while stack:
            top = stack.pop()
            arr.append(top)
            if top in self.graph:
                for neighbor in self.graph[top]:
                    if neighbor not in visited:
                        visited.append(neighbor)
                        stack.append(neighbor)

    def sec_dfs(self, arr, vertex, visited_dfs_back):
        visited = [vertex]
        stack = [vertex]
        while stack:
            top = stack.pop()
            arr.append(top)
            if top in self.graph:
                for neighbor in self.reverse_graph[top]:
                    if neighbor not in visited:
                        if neighbor not in visited_dfs_back:
                            visited.append(neighbor)
                            stack.append(neighbor)

    def add_vertex(self, vertex):
        self.graph[vertex] = []
        self.reverse_graph[vertex] = []

    def add_edge(self, vertex1, vertex2):
        self.graph[vertex1].append(vertex2)
        self.reverse_graph[vertex2].append(vertex1)

    def kosaraju(self, vertex):
        stack_scc = []
        self.dfs(stack_scc, vertex)
        print(stack_scc)
        kosa = []
        visited_dfs_back = set()
        while stack_scc:
            vertex = stack_scc.pop()
            if vertex not in visited_dfs_back:
                print(vertex)
                brr = []
                self.sec_dfs(brr, vertex, visited_dfs_back)
                for i in brr:
                    visited_dfs_back.add(i)
                kosa.append(brr)
        print(kosa)


if __name__ == '__main__':
    g = Graph(5)
    g.add_vertex(1)
    g.add_vertex(2)
    g.add_vertex(3)
    g.add_vertex(4)
    g.add_vertex(5)
    g.add_vertex(6)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(3, 1)
    g.add_edge(2, 4)
    g.add_edge(4, 5)
    g.add_edge(5, 6)
    g.add_edge(6, 4)
    # g.add_edge(1,3)
    # g.add_edge(1,4)
    # g.add_edge(2,1)
    # g.add_edge(3,2)
    # g.add_edge(4,5)
    print(g.graph)
    print(g.reverse_graph)
    g.kosaraju(2)

    # g.kosaraju(0)
