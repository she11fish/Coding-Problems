class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        temp = []
        i = 0
        k = 0
        while i < m and k < n:
            if nums1[i] <= nums2[k]:
                temp.append(nums1[i])
                i += 1
            else:
                temp.append(nums2[k])
                k += 1
        temp = temp + nums1[i:m] + nums2[k:]
        nums1[0:len(nums1)] = temp

        
