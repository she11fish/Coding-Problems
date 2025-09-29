class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return matrix
        m = len(matrix)
        n = len(matrix[0])
        res = []
        start = 0
        while m > 0 and n > 0:
            if start >= n:
                break
            for k in range(start, n):
                res.append(matrix[start][k])
            if start + 1 >= m:
                break
            for k in range(start + 1, m):
                res.append(matrix[k][n - 1])
            if start - 1 >= n - 2:
                break
            for k in range(n - 2, start - 1, -1):
                res.append(matrix[m - 1][k])
            if start >= m - 2:
                break
            for k in range(m - 2, start, -1):
                res.append(matrix[k][start])
            start += 1
            n -= 1
            m -= 1
        return res
