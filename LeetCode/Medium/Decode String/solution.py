class Solution:
    def decodeString(self, s: str) -> str:
        def recurse(s):
            stack = []
            res = []
            print(s)
            for i in range(len(s)):
                if s[i] == "[":
                    stack.append(i)
                    continue
                if s[i] == "]":
                    left = stack.pop()
                    if not stack:
                        right = i
                        if left - 3 >= 0 and s[left - 3:left].isnumeric():
                            res.append(int(s[left - 3:left]) * recurse(s[left + 1:right]))
                        elif left - 2 >= 0 and s[left - 2:left].isnumeric():
                            res.append(int(s[left - 2:left]) * recurse(s[left + 1:right]))
                        else:
                            res.append(int(s[left - 1]) * recurse(s[left + 1:right]))
                    continue
                if not stack and s[i].isalpha():
                    res.append(s[i])
            if not res:
                return s
            return "".join(res)
        return recurse(s)

