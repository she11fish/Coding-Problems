class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        frequency = {}
        for num in nums:
            if num not in frequency:
                frequency[num] = 1
            else:
                frequency[num] += 1
        res = 0
        for key, value in frequency.items():
            if value % k == 0:
               res += value * key
        return res©leetcode
