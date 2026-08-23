# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        @cache
        def dp(node):
            if node is None:
                return (float("inf"), 0, 0)
            left = dp(node.left)
            right = dp(node.right)
            camera = 1 + min(left) + min(right)
            covered = min(
                left[0] + min(right[0], right[1]), right[0] + min(left[0], left[1])
            )
            not_covered = left[1] + right[1]
            return camera, covered, not_covered

        return min(dp(root)[:2])
