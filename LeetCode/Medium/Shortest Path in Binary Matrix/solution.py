class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        def bfs(ox, oy, n, ocounter, visited):
            print(ox, oy)
            queue = [(ox, oy, ocounter)]
            ocounter = float('inf')
            while queue:
                x, y, counter = queue.pop(0)
                if x >= n or y >= n or x < 0 or y < 0:
                    pass
                elif grid[x][y] == 1 or (x, y) in visited:
                    pass
                elif x == n - 1 and y == n - 1:
                    ocounter = min(ocounter, counter)
                else:
                    queue.append((x + 1, y, counter + 1)) 
                    queue.append((x - 1, y, counter + 1))
                    queue.append((x, y + 1, counter + 1))
                    queue.append((x, y - 1, counter + 1))
                    queue.append((x + 1, y + 1, counter + 1))
                    queue.append((x - 1, y + 1, counter + 1))
                    queue.append((x - 1, y - 1, counter + 1))
                    queue.append((x + 1, y - 1, counter + 1))
                visited.add((x, y))
            return ocounter
        ans = bfs(0, 0, len(grid), 1, set())
        if ans == float('inf'):
            return -1
        return ans
