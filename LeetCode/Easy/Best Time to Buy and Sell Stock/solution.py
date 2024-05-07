class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        anchor = 0
        for i in range(1, len(prices)):
            profit = prices[i] - prices[anchor]
            if profit <= 0:
                anchor = i
            max_profit = max(max_profit, profit)
        return max_profit
