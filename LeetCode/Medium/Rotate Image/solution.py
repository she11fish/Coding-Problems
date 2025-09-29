class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return
        def swap(top_left, top_right, bottom_left, bottom_right):
            matrix[top_left[0]][top_left[1]], matrix[top_right[0]][top_right[1]], matrix[bottom_right[0]][bottom_right[1]], matrix[bottom_left[0]][bottom_left[1]] = matrix[bottom_left[0]][bottom_left[1]], matrix[top_left[0]][top_left[1]], matrix[top_right[0]][top_right[1]], matrix[bottom_right[0]][bottom_right[1]]



        n = len(matrix)
        top_left = (0, 0)
        top_right = (0, n - 1)
        bottom_left = (n - 1, 0)
        bottom_right = (n - 1, n - 1)

        while top_left[0] <= bottom_right[0] and top_left[1] <= bottom_right[1] \
                and top_right[0] <= bottom_left[0] and top_right[1] >= bottom_left[1]:
            
            times = bottom_right[1] - top_left[1]
            for i in range(times):
                swap((top_left[0], top_left[1] + i), (top_right[0] + i, top_right[1]), (bottom_left[0] - i, bottom_left[1]), (bottom_right[0], bottom_right[1] - i))
            top_left = top_left[0] + 1, top_left[1] + 1
            top_right = top_right[0] + 1, top_right[1] - 1

            bottom_left = bottom_left[0] - 1, bottom_left[1] + 1 
            bottom_right = bottom_right[0] - 1, bottom_right[1] - 1 
