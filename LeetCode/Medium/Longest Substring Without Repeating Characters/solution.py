class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not len(s):
            return 0
        max_length = 1
        counter = 0
        anchor = 0
        substring = set()
        i = 0
        while i < len(s):
            if s[i] in substring:
                substring = set()
                anchor += 1
                i = anchor
            substring.add(s[i])
            max_length = max(len(substring), max_length)
            i += 1
           
        return max_length
        
