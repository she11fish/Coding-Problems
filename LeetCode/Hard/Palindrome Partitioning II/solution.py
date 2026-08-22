class Solution:
    def minCut(self, s: str) -> int:
        if s[::-1] == s:
            return 0
        memo = {}

        def dp(start):
            if start == len(s):
                return 0
            if start in memo:
                return memo[start]
            best = float("inf")
            for i in range(start + 1, len(s) + 1):
                test = s[start:i]
                if test != test[::-1]:
                    continue
                best = min(dp(i) + 1, best)
            memo[start] = best
            return memo[start]

        return dp(0) - 1
