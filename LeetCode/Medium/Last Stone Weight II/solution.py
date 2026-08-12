class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total_weight = sum(stones)
        target = sum(stones) // 2
        memo = {}
        def dp(i, total):
            if i >= len(stones) or total >= target:
                return abs(total - (total_weight - total))
            if (i, total) in memo:
                return memo[(i, total)]
            memo[(i, total)] = min(dp(i + 1, total), dp(i + 1, total + stones[i]))
            return memo[(i, total)]
        return dp(0, 0)