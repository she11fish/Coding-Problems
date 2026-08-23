class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        visited = set()
        @cache
        def dp(i, j):
            if i == m or j == n or i < 0 or j < 0:
                return 1
            curr = matrix[i][j]
            best = 1
            if ((i + 1), j) not in visited and i + 1 < m and curr < matrix[i + 1][j]:
                visited.add(((i + 1), j))
                best = max(best, dp(i + 1, j) + 1)
                visited.remove(((i + 1), j))
            if ((i - 1), j) not in visited and i - 1 >= 0 and curr < matrix[i - 1][j]:
                visited.add(((i - 1), j))
                best = max(best, dp(i - 1, j) + 1)
                visited.remove(((i - 1), j))
            if (i, (j + 1)) not in visited and j + 1 < n and curr < matrix[i][j + 1]:
                visited.add((i, j + 1))
                best = max(best, dp(i, j + 1) + 1)
                visited.remove((i, j + 1))
            if (i, j - 1) not in visited and j - 1 >= 0 and curr < matrix[i][j - 1]:
                visited.add((i, j - 1))
                best = max(best, dp(i, j - 1) + 1)
                visited.remove((i, j - 1))
            return best
        return max(dp(i, j) for i in range(m) for j in range(n))