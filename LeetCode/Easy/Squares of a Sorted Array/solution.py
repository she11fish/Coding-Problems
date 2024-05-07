class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        r = []
        for num in nums:
            r.append(num ** 2)
        r.sort()
        return r
