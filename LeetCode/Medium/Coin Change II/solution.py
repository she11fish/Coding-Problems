class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}
        def dp(i, remaining):
            if remaining == 0:
                return 1
            if remaining < 0:
                return 0
            if i >= len(coins):
                return 0
            if (i, remaining) in memo:
                return memo[(i, remaining)] 
            memo[(i, remaining)] = dp(i, remaining - coins[i]) + dp(i + 1, remaining)
            return memo[(i, remaining)]
        return dp(0, amount)