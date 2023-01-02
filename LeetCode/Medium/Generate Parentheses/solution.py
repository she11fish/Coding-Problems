class Solution:
    def total_orders(self, n, bracket, result, open_counter = 1, closed_counter = 0):
        print(bracket)
        if open_counter == n and closed_counter == n:
            result.append(bracket)
            return bracket
        left_brackets = []
        right_brackets = []
        if open_counter < n:
            temp_bracket = bracket + "("
            left_brackets = self.total_orders(n, temp_bracket, result, open_counter + 1, closed_counter)
        if closed_counter < n and closed_counter < open_counter:
            temp_bracket = bracket + ")"
            right_brackets = self.total_orders(n, temp_bracket, result, open_counter, closed_counter + 1)
        if not left_brackets and not right_brackets:
            return ""
        if not left_brackets:
            return right_brackets
        if not right_brackets:
            return left_brackets
        return left_brackets + right_brackets

    def generateParenthesis(self, n: int) -> List[str]:
        bracket = "("
        result = []
        self.total_orders(n, bracket, result)
        return result