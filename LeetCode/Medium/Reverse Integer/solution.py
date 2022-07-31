class Solution:
    def reverse(self, x: int) -> int:
        l = list(str(x))[::-1]
        if l[-1] == "-":
            l.pop()
            num = int("".join(l)) * -1
        else:
            num = int("".join(l))
        if num > (2 ** 31) or num < ((-2) ** 31):
            return 0
        return num
        