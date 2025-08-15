class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        end = n + m - 1
        i = m - 1
        k = n - 1
        
        while end >= 0 and i >= 0 and k >= 0:
            if nums1[i] >= nums2[k]:
                nums1[end] = nums1[i]
                i -= 1
            else:
                nums1[end] = nums2[k]
                k -= 1
            end -= 1
            
        while end >= 0 and k >= 0:
            nums1[end] = nums2[k]
            k -= 1
            end -= 1
