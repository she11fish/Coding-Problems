class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            temp = digits[i] + carry
            digits[i] = temp % 10
            carry = temp // 10
        if carry > 0:
            digits.insert(0, carry)
        return digits
