class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def isEdge(x, y):
            return (x == 0 or y == 0) or (x == row_size - 1 or y == col_size - 1) or (x == col_size - 1 and y == row_size - 1)

        def bfs(root, board, ox, oy, row_size, cold_size, visited):
            queue = [(root, ox, oy)]
            board[oy][ox] = "T"
            while queue:
                curr, x, y = queue.pop(0)
                
                dxp = x + 1
                dxn = x - 1
                dyp = y + 1
                dyn = y - 1

                visited.add((x, y))
                
                if dxp >= 0 and dxp < row_size and y >= 0 and y < col_size:
                    if board[y][dxp] == "O" and not (dxp, y) in visited:
                        board[y][dxp] = "T"
                        queue.append((curr, dxp, y))
                if dxn >= 0 and dxn < row_size and y >= 0 and y < col_size:
                    if board[y][dxn] == "O" and not (dxn, y) in visited:
                        board[y][dxn] = "T"
                        queue.append((curr, dxn, y))
                if x >= 0 and x < row_size and dyp >= 0 and dyp < col_size:
                    if board[dyp][x] == "O" and not (x, dyp) in visited:
                        board[dyp][x] = "T"
                        queue.append((curr, x, dyp))
                if x >= 0 and x < row_size and dyn >= 0 and dyn < col_size:
                    if board[dyn][x] == "O" and not (x, dyn) in visited:
                        board[dyn][x] = "T"
                        queue.append((curr, x, dyn))
        col_size = len(board)
        visited = set()
        for y, row in enumerate(board):
            row_size = len(row)
            for x, num in enumerate(row):
                if not (x, y) in visited and isEdge(x, y) and board[y][x] == "O":
                    bfs(num, board, x, y, row_size, col_size, visited)
        for y, row in enumerate(board):
            for x, num in enumerate(row):
                if board[y][x] == "O":
                    board[y][x] = "X"
                if board[y][x] == "T":
                    board[y][x] = "O"
