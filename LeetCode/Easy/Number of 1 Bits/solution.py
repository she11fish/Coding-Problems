class Solution:
    def hammingWeight(self, n: int) -> int:
        num = n
        count = 0
        while num != 0:
            if num & 1:
                count += 1
            num >>= 1
        return count
