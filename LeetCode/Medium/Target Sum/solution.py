class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}

        def dp(i, remaining):
            count = 0
            if remaining == 0:
                count += 1
            if i >= len(nums):
                return count
            if (i, remaining) in memo:
                return memo[(i, remaining)]
            memo[(i, remaining)] = dp(i + 1, remaining - nums[i]) + dp(
                i + 1, remaining + nums[i]
            )
            return memo[(i, remaining)]

        return dp(0, target)
