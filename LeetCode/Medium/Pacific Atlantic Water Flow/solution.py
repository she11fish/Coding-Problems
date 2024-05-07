class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def bfs(root, ox, oy, heights, PO, AO, row_size, col_size, flows, visited):
            queue = [(root, ox, oy)]
            while queue:
                curr, x, y = queue.pop(0)
                dxp = x + 1
                dxn = x - 1
                dyp = y + 1
                dyn = y - 1
                if not PO:
                    PO = (x == 0 or y == 0)
                if not AO:
                    AO = (x == row_size - 1 or y == col_size - 1)
                visited.add((x, y))
                if PO and AO:
                    flows.add((ox, oy))
                    return True
                if (x, y) in flows:
                    return True
                if dxp >= 0 and dxp < row_size and y >= 0 and y < col_size:
                    if heights[y][dxp] <= curr and not (dxp, y) in visited:
                        queue.append((heights[y][dxp], dxp, y))
                if dxn >= 0 and dxn < row_size and y >= 0 and y < col_size:
                    if heights[y][dxn] <= curr and not (dxn, y) in visited:
                        queue.append((heights[y][dxn], dxn, y))
                if x >= 0 and x < row_size and dyp >= 0 and dyp < col_size:
                    if heights[dyp][x] <= curr and not (x, dyp) in visited:
                        queue.append((heights[dyp][x], x, dyp))
                if x >= 0 and x < row_size and dyn >= 0 and dyn < col_size:
                    if heights[dyn][x] <= curr and not (x, dyn) in visited:
                        queue.append((heights[dyn][x], x, dyn))
            return False
        visited = set()
        col_size = len(heights)
        result = []
        flows = set()
        for y, row in enumerate(heights):
            row_size = len(row)
            for x, num in enumerate(row):
                PO = (x == 0 or y == 0)
                AO = (x == row_size - 1 or y == col_size - 1)
                if PO and AO:
                    flows.add((x, y))
                    result.append([y, x])
                elif not (x, y) in visited:
                    if bfs(num, x, y, heights, PO, AO, row_size, col_size, flows, visited):
                        result.append([y, x])
                        flows.add((x, y))
                visited = set()

        return result

