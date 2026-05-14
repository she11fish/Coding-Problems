class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = set()

        def dfs(i):
            if i in visited:
                return
            visited.add(i)
            for j in range(n):
                if isConnected[i][j] == 1:
                    dfs(j)
            return

        s = 0
        for i in range(n):
            if i not in visited:
                s += 1
                dfs(i)
        return s
