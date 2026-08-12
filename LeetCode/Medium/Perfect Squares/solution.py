import math


class Solution:
    def numSquares(self, n: int) -> int:
        nums = []
        for i in range(1, math.ceil(math.sqrt(n)) + 1):
            nums.append(i**2)
        memo = {}

        def dp(remaining):
            if remaining == 0:
                return 0
            if remaining < 0:
                return float("inf")
            if remaining in memo:
                return memo[remaining]
            best = float("inf")
            for i in range(len(nums)):
                best = min(dp(remaining - nums[i]) + 1, best)
            memo[remaining] = best
            return memo[remaining]

        return dp(n)
