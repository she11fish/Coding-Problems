class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        memo = {}

        def dfs(item, visited):
            if item in visited:
                memo[item] = False
                return False
            if item in memo:
                return memo[item]
            visited.add(item)
            t = True
            for e in graph[item]:
                t = t and dfs(e, visited)
            memo[item] = t
            visited.remove(item)
            return t

        res = []
        for i in range(len(graph)):
            if dfs(i, set()):
                res.append(i)
        return res
