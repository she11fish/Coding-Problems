class Solution:
    def f(self, n, memo):
            if n == 0:
                return 0
            if n <= 2:
                return 1
            if n in memo:
                return memo[n]
            else:
                memo[n] = self.f(n - 1, memo) +  self.f(n - 2, memo) + self.f(n - 3, memo)
                return memo[n]
    def tribonacci(self, n: int) -> int:
        memo = {}
        return self.f(n, memo)