class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        def find_max(mini_grid, i, j):
            return max(mini_grid[i - 1][j - 1],
            mini_grid[i - 1][j], mini_grid[i - 1][j + 1],
            mini_grid[i][j - 1], mini_grid[i][j], mini_grid[i][j + 1],
            mini_grid[i + 1][j - 1], mini_grid[i + 1][j], mini_grid[i + 1][j + 1])
        res = []
        for i in range(len(grid)):
            temp = []
            for k in range(len(grid[0])):
                if 0 < i < len(grid) - 1 and 0 < k < len(grid[0]) - 1:
                    temp.append(find_max(grid, i, k))
            if temp:
                res.append(temp)
        return res
