class Solution:
    def countSubstrings(self, s: str) -> int:
        start = 0
        end = len(s) - 1
        dp = [[False] * len(s) for _ in range(len(s))]
        count = 0
        for end in range(len(s)):
            for start in range(end + 1):
                if s[start] == s[end] and (end - start <= 2 or dp[start + 1][end - 1]):
                    dp[start][end] = True
                    count += 1
        return count
