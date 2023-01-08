class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            return -1
        low = 0
        hi = len(nums) - 1
        while low < hi:
            mid = (low + hi) // 2
            if nums[low] == target:
                return low
            if nums[hi] == target:
                return hi
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                low = mid + 1
            if nums[mid] > target:
                hi = mid - 1
        return -1    
