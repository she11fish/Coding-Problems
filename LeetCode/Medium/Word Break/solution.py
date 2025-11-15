class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set()
        for word in wordDict:
            words.add(word)
        memo = {}
        def dp(chars):
            if not chars:
                return True
            if chars in memo:
                return memo[chars]
            res = False
            for i, char in enumerate(chars):
                if chars[:i+1] in words:
                    res = dp(chars[i + 1:])
                if res:
                    memo[chars] = res
                    return True
            memo[chars] = res
            return res

        return dp(s)
