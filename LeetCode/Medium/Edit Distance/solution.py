class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}

        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if i >= len(word1):
                return len(word2) - j
            if j >= len(word2):
                return len(word1) - i
            t = float("inf")
            if word1[i] != word2[j]:
                t = min(t, dp(i + 1, j) + 1, dp(i + 1, j + 1) + 1, dp(i, j + 1) + 1)
            else:
                t = min(t, dp(i + 1, j + 1))
            memo[(i, j)] = t
            return t

        return dp(0, 0)
