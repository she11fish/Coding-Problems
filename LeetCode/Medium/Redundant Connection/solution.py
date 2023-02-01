class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def isTree(og_root, root, parent, graph, visited):
            if root in visited and root == og_root and root != parent:
                return False
            if root in visited:
                return True
            visited.add(root)
            for neighbour in graph[root]:
                if neighbour in visited and neighbour == parent:
                    continue
                boolean = isTree(og_root, neighbour, root, graph, visited)
                if not boolean:
                    return False
            return True
        graph = {}
        for edge in edges:
            if not edge[0] in graph:
                graph[edge[0]] = set()
            graph[edge[0]].add(edge[1])
            if not edge[1] in graph:
                graph[edge[1]] = set()
            graph[edge[1]].add(edge[0])
        for i in range(len(edges) - 1, -1, -1):
            edge = edges[i]
            temp_graph = copy.deepcopy(graph)
            temp_graph[edge[0]].remove(edge[1])
            temp_graph[edge[1]].remove(edge[0])
            if not temp_graph[edge[0]]:
                del temp_graph[edge[0]]
            if not temp_graph[edge[1]]:
                del temp_graph[edge[1]]
            print(temp_graph)
            for node in temp_graph:
                final = isTree(node, node, None, temp_graph, set())
                if not final:
                    break
            if final:
                return edge
        return []
            
