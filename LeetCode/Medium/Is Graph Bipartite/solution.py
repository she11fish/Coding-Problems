class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colors = {}

        def dfs(item, color):
            if item in colors:
                return colors[item] == color
            colors[item] = color
            t = True
            for c in graph[item]:
                t = t and dfs(c, 1 - color)
            return t

        t = True
        for c in range(len(graph)):
            t = t and dfs(c, colors[c] if c in colors else 0)
        return t
