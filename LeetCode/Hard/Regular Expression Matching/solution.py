class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if s == "" and p[0] == "*":
            return True
        if p[0] == "*":
            return False
        memo = {}

        def dp(i, k):
            if i >= len(s):
                if k == len(p):
                    return True
                if k < len(p) - 1 and p[k + 1] == "*":
                    return dp(i, k + 2)
                return False
            if k >= len(p):
                return False
            if (i, k) in memo:
                return memo[(i, k)]

            first_match = (s[i] == p[k]) or (p[k] == ".")

            ans = first_match and (dp(i + 1, k + 1))
            if k < len(p) - 1 and p[k + 1] == "*":
                ans = ans or dp(i, k + 2) or (first_match and dp(i + 1, k))
            memo[(i, k)] = ans
            return ans

        return dp(0, 0)
