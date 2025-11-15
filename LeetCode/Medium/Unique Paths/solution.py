class Solution:
    memo = {}
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        if (m, n) in self.memo:
            return self.memo[(m, n)]
        self.memo[(m, n)] = self.uniquePaths(m - 1, n) + self.uniquePaths(m, n - 1)
        return self.memo[(m, n)]
