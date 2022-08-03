class Solution:
    
    check = False
    def dfs(self, graph, source, destination, visited):
        if source in visited:
            return
        else:
            visited.add(source)
        if source == destination:
            self.check = True
        for neighbour in graph[source]:
            self.dfs(graph, neighbour, destination, visited)
        
    def create_graph(self, edges):
        graph = {}
        for edge in edges:
            if not edge[0] in graph:
                graph[edge[0]] = {edge[1]}
            else:
                graph[edge[0]].add(edge[1])
            if not edge[1] in graph:
                graph[edge[1]] = {edge[0]}
            else:
                graph[edge[1]].add(edge[0])
        return graph
            
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if not edges:
            if source == 0 and destination == 0:
                return True
            return False
        visited = set()
        graph = self.create_graph(edges)
        print(graph)
        self.dfs(graph, source, destination, visited)
        return self.check