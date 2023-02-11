class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def ans(root, cost, i, memo, size):
            if i >= size:
                return minimum
            if i in memo:
                return memo[i]
            if i + 1 < size:
                min_1 = ans(cost[i+1], cost, i + 1, memo, size)
            else:
                min_1 = float('inf')
            if i + 2 < size:
                min_2 = ans(cost[i+2], cost, i + 2, memo, size)
            else:
                min_2 = float('inf')
            min_value = min(min_1, min_2)
            if min_value == float('inf') or min_1 == float('inf') or min_2 == float('inf'):
                memo[i] = root
                return root
            memo[i] = min_value + root
            return min_value + root
        memo = {}
        min1 = ans(cost[0], cost, 0, memo, len(cost))
        min2 = ans(cost[1], cost, 1, memo, len(cost))
        return min(min1, min2)
