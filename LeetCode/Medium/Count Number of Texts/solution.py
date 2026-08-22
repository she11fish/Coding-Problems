class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        mod = 10**9 + 7

        @cache
        def dp(i, count):
            if i == len(pressedKeys):
                return 1
            if i == 0:
                return dp(i + 1, count + 1) % mod
            if pressedKeys[i - 1] == pressedKeys[i] and (
                count < 3 or (count == 3 and (pressedKeys[i] in "79"))
            ):
                return (dp(i + 1, count + 1) + dp(i + 1, 1)) % mod
            return dp(i + 1, 1) % mod

        return dp(0, 0)
