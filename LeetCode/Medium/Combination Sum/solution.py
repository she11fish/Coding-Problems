class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.target = target
        self.nums = candidates
        self.nums.sort()
        return self.backtrack([], 0, 0)

    def backtrack(self, track, acc, i):
        if acc == self.target:
            return track 
        if i >= len(self.nums) or acc > self.target:
            return []
        res = []

        # 1. include next element
        temp = self.backtrack(track + [self.nums[i]], acc + self.nums[i], i)
        if temp:
            if isinstance(temp[0], int):
                res.append(temp)
            else:
                res.extend(temp)
        
        # 3. don't include current element
        temp = self.backtrack(track, acc, i + 1)
        if temp:
            if isinstance(temp[0], int):
                res.append(temp)
            else:
                res.extend(temp)
            
        return res
