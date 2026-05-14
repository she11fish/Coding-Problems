class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)

        def dfs(item, res):
            if item == n - 1:
                res.append(item)
                return res
            res.append(item)
            total = []
            for e in graph[item]:
                t = dfs(e, res.copy())
                if t and type(t[0]) == list:
                    total.extend(t)
                elif t:
                    total.append(t)
            return total

        return dfs(0, [])
