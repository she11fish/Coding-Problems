class Solution:
    def makeGood(self, s: str) -> str:
        stack = [char for char in s]
        i = 0
        while i < len(stack) - 1:
            if stack[i] != stack[i + 1] and stack[i].lower() == stack[i + 1].lower():
                stack.pop(i)
                stack.pop(i)
                if i > 0:
                    i -= 1
                continue
            i += 1
        return "".join(stack)
