class Solution:
    def numTrees(self, n: int) -> int:
        memo = {}

        def factorial(num):
            if num <= 1:
                return num
            memo[num] = num * factorial(num - 1)
            return memo[num]

        return factorial(2 * n) // (factorial(n + 1) * factorial(n))
