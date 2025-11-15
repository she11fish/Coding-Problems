class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return max(nums)
        def dp(index, memo):
            if (0 in memo and index == len(nums) - 1) or index >= len(nums):
                return 0           
            if index in memo:
                return memo[index]
            memo[index] = None
            temp = max(nums[index] + dp(index + 2, memo), dp(index + 1, memo))
            memo[index] = temp
            return temp
        maxval = 0
        for i in range(len(nums)):
            memo = {}
            maxval = max(maxval, dp(i, memo))
        return maxval
