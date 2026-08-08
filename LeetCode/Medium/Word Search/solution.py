class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])

        def dfs(i, j, char_pos, visited):
            if (i, j) in visited:
                return False
            if i < 0 or i >= m or j < 0 or j >= n:
                return False
            if board[i][j] != word[char_pos]:
                return False
            if char_pos == len(word) - 1:
                return True
            visited.add((i, j))
            temp = (
                dfs(i - 1, j, char_pos + 1, visited)
                or dfs(i + 1, j, char_pos + 1, visited)
                or dfs(i, j - 1, char_pos + 1, visited)
                or dfs(i, j + 1, char_pos + 1, visited)
            )
            visited.remove((i, j))
            return temp

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0, set()):
                    return True
        return False
