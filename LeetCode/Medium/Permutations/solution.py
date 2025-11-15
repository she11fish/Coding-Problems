class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(track, visited):
            if len(track) == len(nums):
                res.append(track)
                return
            for i in range(len(nums)):
                if i in visited:
                    continue
                visited.add(i)
                backtrack(track + [nums[i]], visited)
                visited.remove(i)

        backtrack([], set())
        return res
