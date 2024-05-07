class Solution:
    def ans(self, value, memo):
        if value == 1:
            return 10000000
        if value == 2 or value == 3:
            return 1
        if value in memo:
            return memo[value]
        memo[value] = min(self.ans(value - 2, memo), self.ans(value-3, memo)) + 1
        return memo[value]
    def minimumRounds(self, tasks: List[int]) -> int:
        occurences = {}
        for task in tasks:
            if not task in occurences:
                occurences[task] = 1
            else:
                occurences[task] += 1
        result = 0
        for key, value in occurences.items():
            if value == 1:
                return -1
            current_ans = self.ans(value, {})
            result += current_ans
        return result