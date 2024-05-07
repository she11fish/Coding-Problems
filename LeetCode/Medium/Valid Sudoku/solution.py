class Solution:
    
    def check_rows(self, board):
        for l in board:
            duplicates = {}
            for char in l:
                if char in duplicates:
                    return False
                elif char != ".":
                    duplicates[char] = 1
        return True
    
    def check_columns(self, board):
        for i in range(len(board)):
            duplicates = {}
            for l in board:
                if l[i] in duplicates:
                    return False
                elif l[i] != ".":
                    duplicates[l[i]] = 1
        return True
    
    def check_sub_grid(self, board):
        for j in range(3):
            for l in range(3):
                duplicates = {}
                for i in range(j*3, j*3 + 3):
                    for k in range(l*3, l*3 + 3):
                        if board[i][k] in duplicates:
                            return False
                        elif board[i][k] != ".":
                            duplicates[board[i][k]] = 1
        return True
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return self.check_rows(board) and self.check_columns(board) and self.check_sub_grid(board)