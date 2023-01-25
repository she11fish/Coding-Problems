class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(num, coordinates, grid, visited, row_size, col_size):
            x, y = coordinates
            if num == "0" or coordinates in visited:
                return
            visited.add(coordinates)
            dxp = x + 1
            dyp = y + 1
            dxn = x - 1
            dyn = y - 1
            if dxp >= row_size or dxp < 0 or y >= col_size or y < 0:
                pass
            else:
                bfs(grid[y][dxp], (dxp, y), grid, visited, row_size, col_size)
            if dxn >= row_size or dxn < 0 or y >= col_size or y < 0:
                pass
            else:
                bfs(grid[y][dxn], (dxn, y), grid, visited, row_size, col_size)
            if x >= row_size or x < 0 or dyp >= col_size or dyp < 0:
                pass
            else:
                bfs(grid[dyp][x], (x, dyp), grid, visited, row_size, col_size)
            if x >= row_size or x < 0 or dyn >= col_size or dyn < 0:
                pass
            else:
                bfs(grid[dyn][x], (x, dyn), grid, visited, row_size, col_size)
            return
        counter = 0
        visited = set()
        col_size = len(grid)
        for y, row in enumerate(grid):
            row_size = len(row)
            for x, num in enumerate(row):
                if not (x, y) in visited and num == "1":
                    bfs(num, (x,y), grid, visited, row_size, col_size)
                    counter += 1
        return counter
