class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can_find(left, mid, right):   
            hour = 0
            for pile in piles:
                hour += pile // mid
                if pile % mid != 0:
                    hour += 1
            return hour
        right = max(piles)
        left = 1
        while left <= right:
            mid = (right + left) // 2
            hour = can_find(left, mid, right)
            if hour <= h:
                right = mid - 1
            if hour > h:
                left = mid + 1
        return left