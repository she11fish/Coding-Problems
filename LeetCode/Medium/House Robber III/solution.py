# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        @cache
        def dp(node):
            if node is None:
                return 0
            if node.left is not None and node.right is not None:
                return max(
                    node.val
                    + dp(node.left.left)
                    + dp(node.left.right)
                    + dp(node.right.left)
                    + dp(node.right.right),
                    dp(node.left) + dp(node.right),
                )
            elif node.left is not None:
                return max(
                    node.val + dp(node.left.left) + dp(node.left.right),
                    dp(node.left) + dp(node.right),
                )
            elif node.right is not None:
                return max(
                    node.val + dp(node.right.left) + dp(node.right.right),
                    dp(node.left) + dp(node.right),
                )
            return node.val

        return dp(root)
