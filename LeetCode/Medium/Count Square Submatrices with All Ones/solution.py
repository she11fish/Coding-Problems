class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        def all_ones(matrix, n, i, j):
            for l in range(i, i + n):
                for k in range(j, j + n):
                    if matrix[l][k] != 1:
                        return False
            return True
        def num_square_ones(matrix, n):
            count = 0
            row_num = len(matrix)
            col_num = len(matrix[0])
            for i in range(len(matrix)):
                for k in range(len(matrix[0])):
                    if i <= row_num - n and k <= col_num - n and all_ones(matrix, n, i, k):
                        count += 1
            return count
        count = num_square_ones(matrix, 1)
        total_count = count
        i = 2
        n = min(len(matrix), len(matrix[0]))
        while count > 0 and i <= n:
            count = num_square_ones(matrix, i)
            total_count += count
            i += 1
        return total_count
