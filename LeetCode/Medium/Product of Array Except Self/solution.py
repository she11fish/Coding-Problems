class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        product = 1
        for num in nums:
            product *= num
        for i, num in enumerate(nums):
            if num != 0:
                result.append(int(product / num))
            else:
                current_product = 1
                for k in range(len(nums)):
                    if k != i:
                        current_product *= nums[k]
                result.append(current_product)
        return result