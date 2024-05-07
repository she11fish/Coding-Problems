class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occurences = {}
        for num in nums:
            if not num in occurences:
                occurences[num] = 1
            else:
                occurences[num] += 1
        result = []
        for j in range(k):    
            maximum = 0
            for key, value in occurences.items():
                if value > maximum:
                    maximum = value
                    key_of_max = key
            result.append(key_of_max)
            occurences.pop(key_of_max)
        return result