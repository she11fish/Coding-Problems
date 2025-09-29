class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if not mat:
            return mat
        m = len(mat)
        n = len(mat[0])
        if r * c != m * n:
            return mat
        res = []
        for i in range(r):
            temp = []
            for k in range(c):
                temp.append(-99999)
            res.append(temp) 
        i = 0
        k = 0 
        for row in mat:
            for num in row:
                if i < r and k < c:
                    res[i][k] = num
                    k += 1
                elif i < r:
                    i += 1
                    k = 0
                    res[i][k] = num
                    k += 1
        return res
