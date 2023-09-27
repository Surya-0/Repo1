# Given below is the algorithm for identifying Strongly connected components. Find the SCC for the given graph. Your
# implementation should have function which computes transpose of the graph and print the Graph transpose

def mysort(x):
    return x[1]
class Graph:
    def __init__(self):
        self.adList = {}  # direcrted unweighted graph
        self.preTime = {}
        self.postTime = {}

    def add_vertices(self, vertex):
        self.adList[vertex] =[]

    def add_edges(self, s_d_pair):
        self.adList[s_d_pair[0]].append(s_d_pair[1])

    def dfs(self, source, visited, stack):
        global time
        self.preTime[source] = time
        time += 1
        visited.append(source)
        for neighbour in self.adList[source]:
            if neighbour not in visited:
                self.dfs(neighbour, visited, stack)
        stack.append(source)
        self.postTime[source] = time
        time += 1

    def transpose(self):
        transpose = Graph()
        for i in self.adList:
            transpose.adList[i] = []
        for i in self.adList:
            for j in self.adList[i]:
                transpose.adList[j].append(i)
        return transpose

    def sorting_fin_time(self):
        self.dfs(1, [], [])
        vertices_list = list(self.postTime.items())
        vertices_list.sort(key=mysort, reverse=True)
        for i in range(len(vertices_list)):
            vertices_list[i] = vertices_list[i][0]
        return vertices_list

    def scc(self, reversed, sorted):
        scc_list = []
        visited = []

        while sorted:
            v = sorted.pop(0)
            if v not in visited:
                stack = []
                reversed.dfs(v, visited, stack)
                scc_list.append(stack)
        return scc_list


graph = Graph()
vertices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
edges = [(1, 2), (2, 3), (1, 4), (4, 5), (5, 6), (6, 4), (4, 7), (7, 8), (8, 9), (9, 10), (10, 7 )]
for _ in vertices:
    graph.add_vertices(_)

for _ in edges:
    graph.add_edges(_)
print("Given graph: ", graph.adList)

time = 1
print("Vertices sorted based on finish time: ", graph.sorting_fin_time())

scc_list = graph.scc(graph.transpose(), graph.sorting_fin_time())
print("Strongly connected components present: ", scc_list)
