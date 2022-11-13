class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        occurences = []
        for i, word in enumerate(strs):
            occurences.append({})
            for letter in word:
                if not letter in occurences[i]:
                    occurences[i][letter] = 1
                else:
                    occurences[i][letter] += 1

        result = []
        visited = set()
        j = 0

        for i in range(len(occurences)):
            if not strs[i] in visited:
                result.append([strs[i]])
                visited.add(strs[i])
            else:
                j += 1  
                continue
            for k in range(i + 1, len(occurences)):
                if strs[i] == strs[k]:
                    result[i - j].append(strs[i])
                    continue
                if occurences[i] == occurences[k]:
                    result[i - j].append(strs[k])
                    visited.add(strs[k])
        return result