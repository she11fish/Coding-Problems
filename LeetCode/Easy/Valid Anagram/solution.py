class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        occurence_s = {}
        occurence_t = {}

        for char_s in s:
            if not char_s in occurence_s:
                occurence_s[char_s] = 1
            else:
                occurence_s[char_s] += 1
                
        for char_t in t:
            if not char_t in occurence_t:
                occurence_t[char_t] = 1
            else:
                occurence_t[char_t] += 1

        return occurence_s == occurence_t