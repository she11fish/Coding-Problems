class Solution:
    def minInsertions(self, s: str) -> int:
        s1 = s
        s2 = s[::-1]
        memo = {}
        def dp(i, j):
            if i == len(s) or j == len(s):
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            if s1[i] == s2[j]:
                memo[(i, j)]= dp(i + 1, j + 1) + 1
            else:
                memo[(i, j)] = max(dp(i + 1, j), dp(i, j + 1))
            return memo[(i, j)]
        return len(s) - dp(0, 0)