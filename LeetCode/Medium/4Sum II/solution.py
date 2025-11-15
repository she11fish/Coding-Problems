class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        total_nums1 = dict()
        for num1 in nums1:
            for num2 in nums2:
                if num1 + num2 not in total_nums1:
                    total_nums1[num1 + num2] = 1
                else:
                    total_nums1[num1 + num2] += 1
        total_nums2 = dict()
        for num3 in nums3:
            for num4 in nums4:
                if num3 + num4 not in total_nums2:
                    total_nums2[num3 + num4] = 1
                else:
                    total_nums2[num3 + num4] += 1
        count = 0
        for num1 in total_nums1:
            if -num1 in total_nums2:
                count += total_nums1[num1] * total_nums2[-num1]
        return count
