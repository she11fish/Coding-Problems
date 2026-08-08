class WordDictionary:

    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        trie = self.trie
        for char in word:
            if char in trie:
                trie = trie[char]
                continue
            trie[char] = {}
            trie = trie[char]
        trie["#"] = True

    def search(self, word: str) -> bool:
        trie = self.trie

        def helper(i, trie):
            if i == len(word) and "#" in trie:
                return True
            if i == len(word):
                return False
            char = word[i]
            if char in trie:
                trie = trie[char]
                return helper(i + 1, trie)
            if len(trie.keys()) == 0:
                return False
            if char == ".":
                result = False
                for key in trie:
                    if key == "#":
                        continue
                    result = result or helper(i + 1, trie[key])
                return result
            return False

        return helper(0, trie)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
