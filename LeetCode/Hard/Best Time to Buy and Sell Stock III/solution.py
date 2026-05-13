class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}

        def dp(i, state, times):
            if i >= len(prices):
                return 0
            if times >= 2:
                return 0
            if (i, state, times) in memo:
                return memo[(i, state, times)]
            t = 0
            if state == "buy":
                t = max(
                    dp(i + 1, "buy", times), dp(i + 1, "sell", times) - prices[i], t
                )
            if state == "sell":
                t = max(
                    dp(i + 1, "sell", times), dp(i + 1, "buy", times + 1) + prices[i], t
                )
            memo[(i, state, times)] = t
            return t

        return dp(0, "buy", 0)
