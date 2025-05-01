class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for operation in operations:
            if operation.strip("+-").isnumeric():
                stack.append(int(operation))
            if operation == "+":
                if len(stack) >= 2:
                    stack.append(stack[-2] + stack[-1])
                if len(stack) == 1:
                    stack.append(stack[-1])
            if stack and operation == "C":
                stack.pop()
            if stack and operation == "D":
                stack.append(stack[-1] * 2)
        return sum(stack)
