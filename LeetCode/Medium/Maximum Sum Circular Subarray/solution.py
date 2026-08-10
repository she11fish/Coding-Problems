class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        max_memo = {}

        def max_dp(i):
            if i >= len(nums):
                return 0
            if i in max_memo:
                return max_memo[i]
            max_memo[i] = max(max_dp(i + 1) + nums[i], nums[i])
            return max_memo[i]

        min_memo = {}

        def min_dp(i):
            if i >= len(nums):
                return 0
            if i in min_memo:
                return min_memo[i]
            min_memo[i] = min(min_dp(i + 1) + nums[i], nums[i])
            return min_memo[i]

        best_max = max(max_dp(i) for i in range(len(nums)))
        best_min = min(min_dp(i) for i in range(len(nums)))

        if best_max < 0:
            return best_max

        return max(sum(nums) - best_min, best_max)
