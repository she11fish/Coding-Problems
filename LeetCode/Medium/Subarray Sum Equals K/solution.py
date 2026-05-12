class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = {}
        prefix_sum = 0
        m = 0
        for i in range(len(nums)):
            prefix_sum += nums[i]
            if prefix_sum == k:
                m += 1
            if (prefix_sum - k) in d:
                m += d[prefix_sum - k]
            if prefix_sum not in d:
                d[prefix_sum] = 1
            else:
                d[prefix_sum] += 1

        return m
