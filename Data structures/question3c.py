# Given below is the algorithm for identifying Strongly connected components. Find the SCC for the given graph. Your
# implementation should have function which computes transpose of the graph and print the Graph transpose

def mysort(x):
    return x[1]

class Graph:
    def __init__(self):
        self.adList = {}  # direcrted unweighted graph
        self.preTime = {}
        self.postTime = {}

    def add_edges(self, s_d_pair):

        if s_d_pair[0] not in self.adList:
            self.adList[s_d_pair[0]] = []        
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

    def find_max_threshold(self,cities, flights, size):
        left, right = min(cities), max(cities)
        max_threshold = 0  # Initialize the maximum threshold value to 0
        
        while left <= right:
            mid = (left + right) // 2
            
            # Create a graph for the current threshold value
            # graph = Graph()
            # for city in cities:
            #     graph.add_vertices(city)
            # for flight in flights:
            #     if city[0] >= mid and city[1] >= mid:
            #         graph.add_edges(flight)
            
            # Find strongly connected components for the current threshold
            scc_list = graph.scc(graph.transpose(), graph.sorting_fin_time())
            
            # Check if there exists an SCC with size >= s
            for scc in scc_list:
                if len(scc) >= size:
                    max_threshold = mid
                    left = mid + 1
                    break
            else:
                right = mid - 1
        
        return max_threshold

graph = Graph()
n,m,s = 6,7,3
cities = [100,150,68,32,22]
flights = [[1,2],[2,3],[3,4],[4,5],[5,1],[4,6],[6,3]]

for pair in flights:
    graph.add_edges(pair)
print("Given graph: ", graph.adList)

time = 1
print("Vertices sorted based on finish time: ", graph.sorting_fin_time())

scc_list = graph.scc(graph.transpose(), graph.sorting_fin_time())
print("Strongly connected components present: ", scc_list)

result = graph.find_max_threshold(cities, flights, s)
print(result)