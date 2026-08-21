class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        memo = {}
        def dp(i, j):
            if i == len(str1):
                return len(str2) - j
            if j == len(str2):
                return len(str1) - i
            if (i, j) in memo:
                return memo[(i, j)]
            if str1[i] == str2[j]:
               memo[(i, j)] = dp(i + 1, j + 1) + 1
            else:
                memo[(i, j)] = min(dp(i + 1, j), dp(i, j + 1)) + 1
            return memo[(i, j)]
        dp(0, 0)

        i = 0
        j = 0
        res = ""
        while i < len(str1) and j < len(str2):
            if str1[i] == str2[j]:
               res += str1[i]
               i += 1
               j += 1
               continue
            if dp(i + 1, j) <= dp(i, j + 1):
               res += str1[i]
               i += 1
               continue
            res += str2[j]
            j += 1
        res = res + str1[i:] + str2[j:]
        return res
