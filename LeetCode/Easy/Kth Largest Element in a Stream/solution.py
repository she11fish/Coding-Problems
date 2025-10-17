class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = []
        for num in nums:
            if len(self.nums) < k:
                self.nums.append(num)
                self._sift_up(self.nums, len(self.nums) - 1)
            else:
                if num > self.nums[0]:
                    self.nums[0] = num
                    self._sift_down(self.nums, 0)
        
    def _sift_down(self, nums, i):
        l = self.left(i)
        r = self.right(i)

        if l < len(nums) and nums[l] < nums[i]:
            smallest = l
        else:
            smallest = i

        if r < len(nums) and nums[r] < nums[smallest]:
            smallest = r
        
        if smallest != i:
            nums[smallest], nums[i] = nums[i], nums[smallest]
            self._sift_down(nums, smallest)
    
    def _sift_up(self, nums, i):
        p = self.parent(i)

        if p >= 0 and nums[p] > nums[i]:
            nums[i], nums[p] = nums[p], nums[i]
            self._sift_up(nums, p)

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2

    def parent(self, i):
        return (i - 1) // 2

    def extract_min(self, nums):
        if not nums:
            return None
        nums[-1], nums[0] = nums[0], nums[-1]
        minval = nums.pop()
        if nums:
            self._sift_down(nums, 0)
        return minval
        
    def add(self, val: int) -> int:
        if len(self.nums) < self.k:
            self.nums.append(val)
            self._sift_up(self.nums, len(self.nums) - 1)
        elif val > self.nums[0]:
            self.nums[0] = val
            self._sift_down(self.nums, 0)
        return self.nums[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
