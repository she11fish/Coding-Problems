class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return self.backtrack([], nums, 0)

    def backtrack(self, track, nums, i):
        if i >= len(nums):
            return track
        res = []
        temp1 = self.backtrack(track + [nums[i]], nums, i + 1)
        temp2 = self.backtrack(track, nums, i + 1)

        if not temp1 or isinstance(temp1[0], int):
            res.append(temp1)
        else:
            res.extend(temp1)
        if not temp2 or isinstance(temp2[0], int):
            res.append(temp2)
        else:
            res.extend(temp2)

        return res
