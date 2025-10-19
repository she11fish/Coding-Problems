class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total = nums[0]
        temp = nums[0]
        i = 1
        while i < len(nums):
            if nums[i] > 0 and temp <= 0:
                temp = 0
                temp += nums[i]
                total = max(temp, total)
            elif nums[i] > 0:
                temp += nums[i]
                total = max(temp, total)
            else:
                temp += nums[i]  
                total = max(temp, total, nums[i]) 
            i += 1
        return total
