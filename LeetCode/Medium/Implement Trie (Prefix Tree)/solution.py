class Trie:

    def __init__(self):
        self.d = {}

    def insert(self, word: str) -> None:
        def helper(d, word, og_word):
            if word == "":
                d["#"] = og_word
                return
            if word[0] in d:
                helper(d[word[0]], word[1:], og_word)
            else:
                d[word[0]] = {}
                helper(d[word[0]], word[1:], og_word)

        helper(self.d, word, word)

    def search(self, word: str) -> bool:
        def helper(d, word, og_word):
            if word == "":
                if "#" in d and d["#"] == og_word:
                    return True
                return False
            if word[0] in d:
                return helper(d[word[0]], word[1:], og_word)
            else:
                return False

        return helper(self.d, word, word)

    def startsWith(self, prefix: str) -> bool:
        def helper(prefix, d):
            if prefix == "":
                return True
            if prefix[0] in d:
                return helper(prefix[1:], d[prefix[0]])
            else:
                return False
            return helper(word, d)

        return helper(prefix, self.d)


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
