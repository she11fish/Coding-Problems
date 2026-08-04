class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        for i in range(len(time)):
            time[i] = time[i] % 60
        numbers = dict()
        for t in time:
            if t not in numbers:
                numbers[t] = 1
            else:
                numbers[t] += 1
        count = 0
        for num in time:
            numbers[num] -= 1
            if numbers[num] == 0:
                del numbers[num]
            if 60 - num in numbers:
                count += numbers[60 - num]
            if num == 0 and num in numbers:
                count += numbers[num]
        return count
