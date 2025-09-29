class Solution:
    def trap(self, height: List[int]) -> int:
        # Forming any barrier can be defined as
        # Pick l s.t. height[l] > 0
        # Pick r s.t. height[r] > 0
        # max(height[l+1:r]) < min(height[l], height[r])
        # and |l - r| > 1
        # If no such r works for l, then the l+1 block has to be the maximum block between l+1 and r
        # since having that after a distance |l - r| > 1 means it would have been a barrier