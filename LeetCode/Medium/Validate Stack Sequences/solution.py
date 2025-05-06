class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        for i, num in enumerate(pushed):
            stack.append(num)
            curr = num
            while popped and stack and curr == popped[0]:
                stack.pop()
                popped.pop(0)
                if not stack:
                    break
                curr = stack[-1]
        return not popped
