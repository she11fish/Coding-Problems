class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        def ans(root, nums, i, memo, size):
            if i >= size:
                return float('-inf')
            total_max = float('-inf')
            if i in memo:
                return memo[i]
            for k in range(i+2, size):
                curr = ans(nums[k], nums, k, memo, size)
                max_value = max(curr, nums[k])
                if max_value == float('-inf'):
                    memo[i] = max(root, total_max)
                    total_max = max(root, total_max)
                elif curr == float('-inf'):
                    total_max = max(root + nums[k], total_max)
                elif nums[k] == float('-inf'):
                    memo[i] = max(curr + root, total_max)
                    total_max = max(curr + root, total_max)
                else:
                    memo[i] = max(max_value + root, total_max)
                    total_max = max(max_value + root, total_max)
            if total_max == float('-inf'):
                return root
            return total_max
        memo = {}
        
        max1 = ans(nums[0], nums, 0, memo, len(nums))
        max2 = ans(nums[1], nums, 1, memo, len(nums))

        return max(max1, max2)
