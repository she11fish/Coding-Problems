class Solution:
    def add(self, a, b):
        return a + b
    def subtract(self, a, b):
        return a - b
    def multiply(self, a, b):
        return a * b
    def divide(self, a, b):
        return int(a / b)
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = {
            "+": self.add,
            "-": self.subtract,
            "*": self.multiply,
            "/": self.divide
        }
        result = int(tokens[0])
        for token in tokens:
            if token in operations:
                second_num = stack.pop()
                first_num = stack.pop()
                print(first_num, token, second_num)
                result = operations[token](first_num, second_num)
                stack.append(result)
            else:
                stack.append(int(token))
        return result
