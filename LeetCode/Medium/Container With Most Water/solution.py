class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1

        current_area = 0
        max_area = 0

        for i in range(len(height)):
            min_height = min(height[l], height[r])
            current_area = (r - l) * min_height
            if current_area > max_area:
                max_area = current_area
            if height[l] == min_height:
                l += 1
            else:
                r -= 1
        return max_area
