class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        test = set()

        def dp(i, checker, started):
            if i == n:
                return 1
            res = 0
            start = 0
            for j in range(10):
                if not started and j == 0:
                    res += dp(i + 1, checker, False)
                    continue
                if j in checker:
                    continue
                checker.add(j)
                res += dp(i + 1, checker, True)
                checker.remove(j)
            return res

        return dp(0, test, False)
