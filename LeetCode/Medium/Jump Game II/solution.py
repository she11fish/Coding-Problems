class Solution:
    def jump(self, nums: List[int]) -> int:
        memo = {}

        def dp(i):
            if i >= len(nums):
                return -1
            if i == len(nums) - 1:
                return 0
            if i in memo:
                return memo[i]
            t = float("inf")
            for j in range(1, nums[i] + 1):
                s = dp(i + j)
                if s == -1:
                    continue
                t = min(s + 1, t)
            memo[i] = t
            return t

        return dp(0)
