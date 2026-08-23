class Solution:
    def countDigitOne(self, n: int) -> int:
        digits = [int(num) for num in list(str(n))]

        @cache
        def backtrack(i, is_boundary):
            if i == len(digits):
                return 0, 1
            end = None
            if not is_boundary:
                end = 10
            else:
                end = digits[i] + 1
            total_ones = 0
            total_numbers = 0
            for j in range(end):
                ones, numbers = backtrack(i + 1, j == digits[i] and is_boundary)
                total_ones += ones
                if j == 1:
                    total_ones += numbers
                total_numbers += numbers
            return (total_ones, total_numbers)

        return backtrack(0, True)[0]
