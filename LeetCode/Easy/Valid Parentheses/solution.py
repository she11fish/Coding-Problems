class Solution:
    def isValid(self, s: str) -> bool:
        opening_brackets = {"{": "}" , "(": ")", "[": "]"}
        stack = []
        for char in s:
            if char in opening_brackets:
                stack.append(char)
            else:
                if not len(stack):
                    return False
                current_char = stack.pop()
                while True:
                    if current_char in opening_brackets:
                        if opening_brackets[current_char] == char:
                            break
                        else:
                            return False
                    if not len(stack):
                        return False
                    current_char = stack.pop()
        return not len(stack)
