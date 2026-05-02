class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}

        def dfs(i, state):
            if i >= len(prices):
                return 0
            if (i, state) in memo:
                return memo[(i, state)]
            if state == "nothing":
                t = max(dfs(i + 1, "nothing"), dfs(i + 1, "buying") - prices[i])
                memo[(i, state)] = t
                return t
            if state == "buying":
                t = max(dfs(i + 1, "selling") + prices[i], dfs(i + 1, "buying"))
                memo[(i, state)] = t
                return t
            if state == "selling":
                t = dfs(i + 1, "nothing")
                memo[(i, state)] = t
                return t

        t = dfs(0, "nothing")
        return t
