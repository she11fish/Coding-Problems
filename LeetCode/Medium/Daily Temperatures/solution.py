class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [(0, temperatures[0])]
        result = [0 for i in range(len(temperatures))]
        for i in range(1, len(temperatures)):
            if temperatures[i] > stack[-1][1]:
                while len(stack) and temperatures[i] > stack[-1][1]:
                    top_index = stack[-1][0]
                    result[top_index] = i - top_index 
                    stack.pop()
            stack.append((i, temperatures[i]))
        return result
