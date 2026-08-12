class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}

        def dp(i, j):
            if i == len(text2) or j == len(text1):
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            best = dp(i, j + 1)
            if text1[j] == text2[i]:
                best = max(dp(i + 1, j + 1) + 1, best)
            else:
                best = max(best, dp(i + 1, j))
            memo[(i, j)] = best
            return best

        return dp(0, 0)
