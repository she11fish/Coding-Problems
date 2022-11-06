class Solution:
    def ans(self, n: int, memo):
        if (n <= 2):
            return n
        if n in memo:
            return memo[n]
        memo[n] = self.ans(n-1, memo) + self.ans(n-2, memo)
        return memo[n]

    def climbStairs(self, n: int) -> int:
        return self.ans(n, {})