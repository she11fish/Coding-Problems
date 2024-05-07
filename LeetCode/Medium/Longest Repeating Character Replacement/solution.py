class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        anchor = 0
        i = 0
        result = 0
        counter = {}
        counter[s[i]] = 1
        while i < len(s):
            window_length = i - anchor + 1
            temp_result = window_length - max(counter.values())
            if temp_result <= k:
                result = max(result, window_length)
                i += 1
                if i >= len(s):
                    break
                if not s[i] in counter:
                    counter[s[i]] = 1
                else:
                    counter[s[i]] += 1
            else:
                counter[s[anchor]] -= 1
                anchor += 1
        return result
