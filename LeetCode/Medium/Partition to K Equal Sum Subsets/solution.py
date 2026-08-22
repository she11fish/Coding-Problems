class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        s = sum(nums)
        if s % k != 0:
            return False
        target = s / k

        visited = set()
        
        def dp(i, total, groups):
            if groups == 0:
                return True
            if total == target:
                return dp(0, 0, groups - 1)
            for j in range(i, len(nums)):
                if j in visited or total + nums[j] > target:
                    continue
                visited.add(j)
                if dp(j + 1, total + nums[j], groups):
                    return True
                visited.remove(j)
                if total == 0:
                    break
            return False
        return dp(0, 0, k)