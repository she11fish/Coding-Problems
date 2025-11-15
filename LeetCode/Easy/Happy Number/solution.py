class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while n != 1 and n not in visited:
            total = 0
            for k in str(n):
                total += int(k) ** 2
            visited.add(n)
            n = total
        return n == 1
