class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        min_contiguous = [float('inf')] * (len(nums))
        min_contiguous[0] = nums[0]

        max_contiguous = [float('-inf')] * (len(nums))
        max_contiguous[0] = nums[0]

        dp = [-1 for _ in range(len(nums))]
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            if min_contiguous[i - 1] != float('inf'):
                min_contiguous[i] = min(min_contiguous[i - 1] * nums[i], nums[i], max_contiguous[i - 1] * nums[i])
            else:
                min_contiguous[i] = nums[i - 1]

            if max_contiguous[i - 1] != float('-inf'):
                max_contiguous[i] = max(max_contiguous[i - 1] * nums[i], nums[i], min_contiguous[i - 1] * nums[i])
            else:
                max_contiguous[i] = nums[i - 1]

            dp[i] = max(dp[i - 1], max_contiguous[i], min_contiguous[i], nums[i])

        return dp[-1]
