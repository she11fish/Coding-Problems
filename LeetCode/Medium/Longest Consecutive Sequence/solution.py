class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_of_num = set(nums)
        visited = set()

        i = 0

        if not nums:
            return 0

        num = nums[i]
        representatives = []

        while i < len(nums):
            if num in visited:
                i += 1
                if i == len(nums):
                    break
                num = nums[i]

            if num + 1 in set_of_num:
                visited.add(num)
                num += 1
            else:
                i += 1
                if num - 1 in set_of_num:
                    representatives.append(num)
                if i == len(nums):
                    break
                num = nums[i]
        print(representatives)
        print(set_of_num)
        counter = 1
        maximum = 0
        i = 0
        if not representatives:
            return 1
        num = representatives[i]
        while i < len(representatives):
            if num - 1 in set_of_num:
                counter += 1
                visited.add(num)
                num -= 1
            else:
                i += 1
                print(maximum)
                if counter > maximum:
                    maximum = counter
                counter = 1
                if i == len(representatives):
                    break
                num = representatives[i]
        return maximum
