class Graph:  # a class for graph construction
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        for i in vertex:
            self.graph[i] = []

    def add_edge(self, edges):
        for i in edges:
            self.graph[i[0]].append(i[1])
            self.graph[i[1]].append(i[0])


# Issafe function for creating a graph

def issafe(model, color, v, c):
    for vert in model.graph[v]:
        if color[vert] == c:
            return False
    return True


# Kcolorable function for coloring the graph
def kcolorable(model, color, k, v, c):
    if v == n:
        print(color)
        return

    for c in range(k):
        if issafe(model, color, v, c):
            color[v] = c

            kcolorable(model, color, k, v + 1, c)  # recursion

            color[v] = 0  # backtracking


if __name__ == '__main__':
    vertex = [0, 1, 2, 3, 4, 5]
    edges = [(0, 1), (0, 4), (0, 5), (4, 5), (1, 4), (1, 3), (2, 3), (2, 4)]
    model = Graph()
    model.add_vertex(vertex)
    model.add_edge(edges)
    Colors = ['Blue', 'Green', 'Red']
    n = 6  # number of vertices
    k = 3  # number of colors
    color = [None] * n
    kcolorable(model, color, k, 0, n)
    # v is the vertex
    # model is the graph object
    # k is the number of colors
    # n is the number of vertices
    # print(model.graph)
