class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        hi = len(nums) - 1
        while low < hi:
            mid = (low + hi) // 2
            print(low, mid, hi)
            if nums[mid] == nums[low]:
                if nums[low] > nums[hi]:
                    return nums[hi]
                else:
                    return nums[low]
            if nums[low] > nums[hi]:
                if nums[mid] > nums[low]:
                    low = mid
                else:
                    hi = mid
            else:
                return nums[low]
        return nums[hi]
