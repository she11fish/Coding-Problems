class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        checker = set(words)
        memo = {}

        def dp(start, word):
            if start == len(word):
                return True
            if start in memo:
                return memo[start]
            best = False
            for i in range(start + 1, len(word) + 1):
                if not best and word[start:i] in checker:
                    best = dp(i, word)
            memo[start] = best
            return best

        min_size = len(min(words, key=lambda e: len(e)))
        res = []
        for i, word in enumerate(words):
            if len(word) == min_size:
                continue
            memo = {}
            checker.remove(word)
            if dp(0, word):
                res.append(word)
            checker.add(word)
        return res
