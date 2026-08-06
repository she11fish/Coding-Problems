class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freq = {}
        for char in t:
            if char not in freq:
                freq[char] = 1
            else:
                freq[char] += 1
        check = {}
        for item in freq:
            check[item] = 0
        l = 0
        best = float('inf')
        best_str = ""
        for r in range(len(s)):
            if s[r] in freq:
                if s[r] not in check:
                    check[s[r]] = 1
                else:
                    check[s[r]] += 1
            is_satisfied = True
            for entry in check:
                    if check[entry] < freq[entry]:
                        is_satisfied = False
                        break
            while is_satisfied and (s[l] not in freq or check[s[l]] > freq[s[l]]):
                if s[l] in freq:
                    check[s[l]] -= 1
                for entry in check:
                    if check[entry] < freq[entry]:
                        is_satisfied = False
                        break
                l += 1 
            if is_satisfied:
                if best > r - l + 1:
                    best = r - l + 1
                    best_str = s[l: r + 1]
        return best_str