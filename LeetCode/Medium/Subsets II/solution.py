class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def backtrack(track, i):
            if i >= len(nums):
                res.append(track)
                return
            backtrack(track + [nums[i]], i + 1)
            j = i + 1
            while j < len(nums) and nums[j] == nums[i]:
                j += 1
            backtrack(track, j)
        backtrack([], 0)
        return res
