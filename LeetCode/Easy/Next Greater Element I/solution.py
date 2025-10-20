class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        res = [-1] * len(nums1)
        d = {}
        for i, num1 in enumerate(nums1):
            d[num1] = i
        for i, num2 in enumerate(nums2):
            while stack and nums2[i] > nums2[stack[-1]]:
                value = stack.pop()
                if nums2[value] in d:
                    res[d[nums2[value]]] = nums2[i]
            stack.append(i)
        return res
