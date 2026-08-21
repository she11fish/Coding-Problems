class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        memo = {}

        def dp(i):
            if i in memo:
                return memo[i]
            counter = 1
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    counter = max(dp(j) + 1, counter)
            memo[i] = counter
            return counter

        target = max([dp(i) for i in range(len(nums))])
        count_memo = {}

        def dp_res(i):
            if i in count_memo:
                return count_memo[i]
            if dp(i) == 1:
                return 1
            times = 0
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j] and dp(j) == dp(i) - 1:
                    times += dp_res(j)
            count_memo[i] = times
            return times

        return sum(dp_res(i) for i in range(len(nums)) if dp(i) == target)
