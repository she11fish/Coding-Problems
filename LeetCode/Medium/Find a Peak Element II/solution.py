class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])

        end = n - 1
        start = 0
        while start <= end:
            mid = (end + start) // 2
            largest = 0
            for i in range(m):
                if mat[i][mid] > mat[largest][mid]:
                    largest = i
            left = mat[largest][mid - 1] if mid - 1 >= 0 else -1
            right = mat[largest][mid + 1] if mid + 1 < n else -1
            pivot = mat[largest][mid]
            if left < pivot and right < pivot:
                return [largest, mid]
            if left > pivot:
                end = mid - 1
            if right > pivot:
                start = mid + 1
