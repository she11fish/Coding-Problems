class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        start = 0
        middle = len(nums) // 2
        result = []
        for i in range(len(nums) // 2):
            result.append(nums[start])
            result.append(nums[middle])
            start += 1
            middle += 1
        return result