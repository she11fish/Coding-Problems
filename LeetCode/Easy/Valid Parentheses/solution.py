class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {
            "(": ")",
            "[": "]",
            "{": "}"

        }
        for char in s:
            if char in brackets:
                stack.append(char)
                continue
            if not stack or brackets[stack[-1]] != char:
                return False
            stack.pop()
        return not stack
