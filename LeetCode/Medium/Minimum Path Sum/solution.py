class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        memo = {}

        def dp(i, j):
            if i == len(grid) - 1 and j == len(grid[0]) - 1:
                return grid[i][j]
            if (i, j) in memo:
                return memo[(i, j)]
            t = float("inf")
            if i < len(grid) - 1:
                t = min(dp(i + 1, j) + grid[i][j], t)
            if j < len(grid[0]) - 1:
                t = min(dp(i, j + 1) + grid[i][j], t)
            memo[(i, j)] = t
            return t

        return dp(0, 0)
