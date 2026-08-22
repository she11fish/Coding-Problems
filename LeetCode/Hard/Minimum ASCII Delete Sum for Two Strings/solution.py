class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        memo = {}

        def dp(i, j):
            if i == len(s1):
                return sum([ord(c) for c in s2[j:]])
            if j == len(s2):
                return sum([ord(c) for c in s1[i:]])
            if (i, j) in memo:
                return memo[(i, j)]
            if s1[i] == s2[j]:
                memo[(i, j)] = dp(i + 1, j + 1)
            else:
                memo[(i, j)] = min(dp(i + 1, j) + ord(s1[i]), dp(i, j + 1) + ord(s2[j]))
            return memo[(i, j)]

        return dp(0, 0)
