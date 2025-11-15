class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        memo = {}
        def dp(i, sum1, sum2):
            if sum1 == sum2:
                return True
            if sum1 > sum2:
                return False
            if i == len(nums):
                return False
            if (i, sum1) in memo:
                return memo[(i, sum1)]
            num = nums[i]
            if dp(i + 1, sum1 + num, sum2 - num) or dp(i + 1, sum1, sum2):
                memo[(i, sum1)] = True
                return True
            memo[(i, sum1)] = False
            return False
        return dp(1, nums[0], sum(nums) - nums[0])
