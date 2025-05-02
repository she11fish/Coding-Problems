class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        result = []
        for i in range(len(prices)):
            other_price = 0
            for j in range(i + 1, len(prices)):
                if prices[j] <= prices[i]:
                    other_price = prices[j]
                    break
            result.append(prices[i] - other_price)
        return result
