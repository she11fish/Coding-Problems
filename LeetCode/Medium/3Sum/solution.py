class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        print(sorted_nums)
        result = []
        for i in range(len(sorted_nums)):
            if sorted_nums[i - 1] == sorted_nums[i] and i > 0:
                continue
            left = i + 1
            right = len(sorted_nums) - 1
            while left < right:
                total = sorted_nums[i] + sorted_nums[left] + sorted_nums[right]
                if total == 0:
                    result.append([sorted_nums[i], sorted_nums[left], sorted_nums[right]])
                    left += 1
                    while sorted_nums[left] == sorted_nums[left - 1] and left < right:
                        left += 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
        return result
