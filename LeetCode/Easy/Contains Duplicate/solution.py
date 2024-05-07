class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        duplicates = {}
        for num in nums:
            if not num in duplicates:
                duplicates[num] = 1
            else:
                return True
        return False