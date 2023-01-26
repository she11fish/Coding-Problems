class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def bfs(root, coordinates, grid, row_size, col_size, visited):
            x, y = coordinates
            if root == 0 or coordinates in visited:
                return 0
            visited.add(coordinates)
            queue = [(root, x, y)]
            counter = 1
            while queue:
                curr, x, y = queue.pop(0)
                dxp = x + 1
                dxn = x - 1
                dyp = y + 1
                dyn = y - 1
                if dxp < row_size and dxp >= 0 and y < col_size and y >= 0:
                    if not (dxp, y) in visited: 
                        if grid[y][dxp]: 
                            counter += 1
                            visited.add((dxp, y))
                            queue.append((grid[y][dxp], dxp, y))
                if dxn < row_size and dxn >= 0 and y < col_size and y >= 0:
                    if not (dxn, y) in visited:
                        if grid[y][dxn]: 
                            counter += 1 
                            visited.add((dxn, y))
                            queue.append((grid[y][dxn], dxn, y))
                if x < row_size and x >= 0 and dyp < col_size and dyp >= 0:
                    if not (x, dyp) in visited:  
                        if grid[dyp][x]: 
                            counter += 1
                            visited.add((x, dyp))
                            queue.append((grid[dyp][x], x, dyp))
                if x < row_size and x >= 0 and dyn < col_size and dyn >= 0:
                    if not (x, dyn) in visited:
                        if grid[dyn][x]: 
                            counter += 1
                            visited.add((x, dyn))  
                            queue.append((grid[dyn][x], x, dyn))
            return counter           
        visited = set()
        col_size = len(grid)
        counter = 0
        for y, row in enumerate(grid):
            row_size = len(row)
            for x, num in enumerate(row):
                if not (x, y) in visited and num == 1:
                    counter = max(counter, bfs(num, (x, y), grid, row_size, col_size, visited)) 
        return counter
