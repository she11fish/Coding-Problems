class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        graph = {}
        maximum = 0
        for edge in edges:
            if not edge[0] in graph:
                graph[edge[0]] = {edge[1]}
            else:
                graph[edge[0]].add(edge[1])
                
            length = len(graph[edge[0]])
            if length > maximum:
                maximum = length
                key = edge[0]
    
            if not edge[1] in graph:
                graph[edge[1]] = {edge[0]}
            else:
                graph[edge[1]].add(edge[0])
                
            length = len(graph[edge[1]])
            if length > maximum:
                maximum = length
                key = edge[1]
        return key