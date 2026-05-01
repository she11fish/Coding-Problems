class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        freq = {}
        for c in s:
            if c not in freq:
                freq[c] = 1
            else:
                freq[c] += 1
        stack = []
        visited = set()
        for i in range(len(s)):
            freq[s[i]] -= 1
            if s[i] in visited:
                continue
            while stack and s[i] < stack[-1] and freq[stack[-1]] > 0:
                visited.remove(stack.pop())
            stack.append(s[i])
            visited.add(s[i])
        return "".join(stack)
