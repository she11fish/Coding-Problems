class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat:
            return []
        res = []
        has_down = True
        has_right = True
        i = 0
        k = 0
        m = len(mat)
        n = len(mat[0])
        is_up = True
        while (i, k) != (m, n):
            if is_up:
                while 0 <= (i - 1) < m and (k + 1) < n:
                    res.append(mat[i][k])
                    i -= 1
                    k += 1
                # has right
                res.append(mat[i][k])
                if (k + 1) < n:
                    k += 1
                # has down
                elif (i + 1) < m:
                    i += 1
                else:
                    break
                is_up = False
            else:
                while (i + 1) < m and 0 <= (k - 1) < n:
                    res.append(mat[i][k])
                    i += 1
                    k -= 1
                is_up = True
                res.append(mat[i][k])
                # has down
                if (i + 1) < m:
                    i += 1
                # has right
                elif (k + 1) < n:
                    k += 1
                else:
                    break
                is_up = True
        return res
