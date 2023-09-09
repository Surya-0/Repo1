import heapq
class Graph:
    def __init__(self):
        self.graph = {}
        self.weights = {}
    
    def add_vertex(self, vertex):
        self.graph[vertex]=[]
    
    def add_edge(self,vertex1,vertex2,weight):
        self.graph[vertex1]=vertex2
        self.graph[vertex2]=vertex1
        self.weights[(vertex1,vertex2)]=weight
        self.weights[(vertex2,vertex1)]=weight
    
    def djikstras(self,source):
        distances= {}
        for vertex in self.graph:
            distances[vertex]=float('inf')
        
        distances[source]=0
        priority_queue = [(0,source)]
        while priority_queue:
            pop_distance,pop_vertex = heapq.heappop(priority_queue)
            for adjacent_vertex in self.graph[pop_vertex]:
                new_distance = distances[pop_vertex]+self.weights[(pop_vertex,adjacent_vertex)]
                
                if  new_distance < distances[adjacent_vertex]:
                    distances[adjacent_vertex] = new_distance
                    heapq.heappush(priority_queue, (new_distance,adjacent_vertex))
        return distances
                
        
        