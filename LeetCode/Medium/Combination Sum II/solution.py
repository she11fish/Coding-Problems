class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        nums = candidates
        nums.sort()
        res = []

        def backtrack(track, acc, i):
            if acc == target:
                res.append(track)
                return
            if acc > target:
                return []
            if i >= len(nums):
                return []
            backtrack(track + [nums[i]], acc + nums[i], i + 1)

            j = i
            while j < len(nums) and nums[j] == nums[i]:
                j += 1
            backtrack(track, acc, j)
        backtrack([], 0, 0)

        return res
