class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        start = 0
        end = len(nums)
        self.merge(nums, start, end)

    def merge(self, lst, start, end):
        if end - start <= 1:
            return
        middle = (start + end) // 2
        self.merge(lst, start, middle)
        self.merge(lst, middle, end)
        self._merge(lst, start, middle, end)

    def _merge(self, lst, start, middle, end):
        temp = []
        i = start
        k = middle
        while i < middle and k < end:
            if lst[i] <= lst[k]:    
                temp.append(lst[i])
                i += 1
            else:
                temp.append(lst[k])
                k += 1
        while i < middle:
            temp.append(lst[i])
            i += 1
        while k < end:
            temp.append(lst[k])
            k += 1   
        lst[start:end] = temp
