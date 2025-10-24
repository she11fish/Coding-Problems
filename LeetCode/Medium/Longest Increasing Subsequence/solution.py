class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * (len(nums))
        for i in range(1, len(nums)):
            maxLIS = 0
            for k in range(i):
                if nums[i] > nums[k]:
                    maxLIS = max(dp[k], maxLIS)
            dp[i] = maxLIS + 1
        return max(dp)
