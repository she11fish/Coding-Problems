class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}
        def dp(i):
            if i in memo:
                return memo[i]
            if i == len(s):
                return 1
            if i >= len(s) or s[i] == "0":
                return 0
            if s[i] > "2" or (s[i] == "2" and i < len(s) - 1 and s[i + 1] > "6"):
                memo[i] = dp(i + 1)
                return memo[i]
            count = 0
            if i < len(s) - 1 and ((s[i] == "2" and s[i + 1] <= "6") or s[i] < "2"):
                count += dp(i + 2)
            count += dp(i + 1)
            memo[i] = count
            return memo[i]
        return dp(0)
