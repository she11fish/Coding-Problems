class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for log in logs:
            if log not in ["./", "../"]:
                stack.append(log)
                continue
            if stack and log == "../":
                stack.pop()
        return len(stack)
