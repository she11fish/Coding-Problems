class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        total = nums[0]
        for num in nums[1:]:
            total ^= num
        return total
