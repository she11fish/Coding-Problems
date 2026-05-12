class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        prefix_sum = 0
        d = {}
        m = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                prefix_sum -= 1
            else:
                prefix_sum += 1
            if prefix_sum == 0:
                m = max(m, i + 1)
            if prefix_sum in d:
                m = max(m, i - d[prefix_sum])
            else:
                d[prefix_sum] = i
        return m
