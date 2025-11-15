class Solution:
    def minMoves(self, nums: List[int]) -> int:
        max_num = max(nums)
        sum = 0 
        for num in nums:
            sum += max(max_num - num, 0)
        return sum©leetcode
