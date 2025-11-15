class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        def is_diagonal(i, k):
            temp = matrix[i][k]
            while i < len(matrix) and k < len(matrix[0]):
                if temp != matrix[i][k]:
                    return False
                i += 1
                k += 1
            return True
        i = len(matrix) - 1
        k = 0
        while i > 0 or k < len(matrix[0]):
            if not is_diagonal(i, k):
                return False
            if i > 0:
                i -= 1
            else:
                k += 1
        return True
