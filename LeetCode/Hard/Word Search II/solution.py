class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m = len(board)
        n = len(board[0])
        self.trie = {}
        visited = set()
        res = set()

        def search(i, j, trie, visited) -> None:
            if i < 0 or i >= m or j < 0 or j >= n:
                return
            char = board[i][j]
            if char not in trie:
                return
            if (i, j) in visited:
                return
            visited.add((i, j))

            trie = trie[char]
            if "#" in trie:
                res.add(trie["#"])
                del trie["#"]

            search(i - 1, j, trie, visited)
            search(i + 1, j, trie, visited)
            search(i, j - 1, trie, visited)
            search(i, j + 1, trie, visited)
            visited.remove((i, j))

        def add_word(word) -> None:
            trie = self.trie
            for char in word:
                if char not in trie:
                    trie[char] = {}
                trie = trie[char]
            trie["#"] = word

        for word in words:
            add_word(word)
        visited = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                search(i, j, self.trie, visited)
        return list(res)
