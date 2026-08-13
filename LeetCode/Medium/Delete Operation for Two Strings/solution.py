class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}

        def dp(i, j):
            if i == len(word1):
                return len(word2) - j
            if j == len(word2):
                return len(word1) - i
            if (i, j) in memo:
                return memo[(i, j)]
            best = float("inf")

            if word1[i] == word2[j]:
                best = dp(i + 1, j + 1)
            else:
                best = 1 + min(dp(i + 1, j), dp(i, j + 1))
            memo[(i, j)] = best
            return best

        return dp(0, 0)
