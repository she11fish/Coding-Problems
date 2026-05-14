class Solution:
    def canJump(self, nums: List[int]) -> bool:
        memo = {}

        def dp(i):
            if i >= len(nums):
                return False
            if i == len(nums) - 1:
                return True
            if i in memo:
                return memo[i]
            if nums[i] >= len(nums) - i:
                return True
            t = False
            for k in range(i + 1, i + nums[i] + 1):
                if k >= len(nums):
                    break
                t = t or dp(k)
            memo[i] = t
            return t

        return dp(0)
