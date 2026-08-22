class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        memo = {}

        @cache
        def dp(i, j):
            return min(
                (
                    dp(i, k) + values[i] * values[k] * values[j] + dp(k, j)
                    for k in range(i + 1, j)
                ),
                default=0,
            )

        return dp(0, len(values) - 1)
