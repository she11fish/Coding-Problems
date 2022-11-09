class Solution:
    def check_space(self, char1, char2):
        roman_numerals = ["I", "V", "X", "L", "C", "D", "M"]
        current_index = roman_numerals.index(char1)
        return roman_numerals[current_index + 1] == char2 or roman_numerals[current_index + 2] == char2 
    def romanToInt(self, s: str) -> int:
        result = 0
        d = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        base_10 = {"I","X","C"}
        i = 0
        while i < len(s):
            char = s[i]
            if char in base_10 and i != len(s) - 1:
                if (d[s[i+1]] > d[char] and self.check_space(char, s[i+1])):
                    result += d[s[i+1]] - d[char]
                    i += 1
                else:
                    result += d[char]
            else:
                result += d[char]
            i += 1
        return result
