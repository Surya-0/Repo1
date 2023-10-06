class Graph:
    def __init__(self):
        self.graph={}
    
    def add_vertex(self,vertex):
        self.graph[vertex] = []
    
    def add_edge(self,vertex1,vertex2):
        self.graph[vertex1].append(vertex2)
    
    def dfs_trav(self,vertex):
        stack = [vertex]
        visited = [vertex]
        
        while stack:
            vert = stack.pop()
            print(vert)
            for neighbor in self.graph[vert]:
                if neighbor not in visited:
                    visited.append(neighbor)
                    stack.append(neighbor)
    
    def bfs_trav(self,vertex):
        queue = [vertex]
        visited = [vertex]
        
        while queue:
            vert = queue.pop(0)
            print(vert)
            for neighbor in self.graph[vert]:
                if neighbor not in visited:
                    visited.append(neighbor)
                    queue.append(neighbor)
    
    def print_graph(self):
        for vertex in self.graph:
            print(vertex," : ",self.graph[vertex])    
    
    def topological_sort(self):
        in_degree = {}
        for vertex in self.graph:
            in_degree[vertex] = 0 
        
        for vertex1 in self.graph:
            for vertex2 in self.graph[vertex1]:
                in_degree[vertex2]+=1
        
        # print(in_degree)
        queue = []
        topological_sort = []
        for vertex in in_degree:
            if in_degree[vertex] == 0:
                queue.append(vertex)
        while queue:
            element = queue.pop(0)
            topological_sort.append(element)
            
            for vertex in self.graph[element]:
                in_degree[vertex]-=1
                if in_degree[vertex] == 0:
                    queue.append(vertex)
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
graph.dfs_trav('A')
print("BFS traversal : ")
graph.bfs_trav('A')
print("Topological sort : ")
print(graph.topological_sort())
                    
        
    
    