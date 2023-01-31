class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def bfs(root, grid, ox, oy, row_size, col_size, oranges, counter, visited):
            queue = [(root, ox, oy)]
            while queue:
                curr, x, y = queue.pop(0)
                
                dxp = x + 1
                dxn = x - 1
                dyp = y + 1
                dyn = y - 1

                visited.add((x, y))

                if dxp >= 0 and dxp < row_size and y >= 0 and y < col_size:
                    if grid[y][dxp] == 1 and not (dxp, y) in visited:
                        grid[y][dxp] = counter + 3
                        if (dxp, y) in oranges:
                            oranges.remove((dxp, y))
                if dxn >= 0 and dxn < row_size and y >= 0 and y < col_size:
                    if grid[y][dxn] == 1 and not (dxn, y) in visited:
                        grid[y][dxn] = counter + 3
                        if (dxn, y) in oranges:
                            oranges.remove((dxn, y))
                if x >= 0 and x < row_size and dyp >= 0 and dyp < col_size:
                    if grid[dyp][x] == 1 and not (x, dyp) in visited:
                        grid[dyp][x] = counter + 3
                        if (x, dyp) in oranges:    
                            oranges.remove((x, dyp))
                if x >= 0 and x < row_size and dyn >= 0 and dyn < col_size:
                    if grid[dyn][x] == 1 and not (x, dyn) in visited:
                        grid[dyn][x] = counter + 3
                        if (x, dyn) in oranges:
                            oranges.remove((x, dyn))
        col_size = len(grid)
        visited = set()
        counter = 0
        prev_grid = []
        oranges = set()
        while prev_grid != grid:
            prev_grid = copy.deepcopy(grid)
            for y, row in enumerate(grid):
                row_size = len(row)
                for x, num in enumerate(row):
                    if num == 1:
                        oranges.add((x, y))
                    if not (x, y) in visited and num == counter + 2:
                        bfs(num, grid, x, y, row_size, col_size, oranges, counter, visited)
            counter += 1
        if oranges:
            return -1
        return counter - 1
