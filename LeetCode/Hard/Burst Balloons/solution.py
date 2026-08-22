class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        memo = {}
        nums.append(1)
        nums.insert(0, 1)

        @cache
        def dp(i, j):
            return max(
                (
                    dp(i, k) + nums[i] * nums[k] * nums[j] + dp(k, j)
                    for k in range(i + 1, j)
                ),
                default=0,
            )

        return dp(0, len(nums) - 1)
