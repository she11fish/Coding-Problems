# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        total = float("-inf")
        def dfs(root):
            nonlocal total
            if not root:
                return 0
            max_left_path = max(dfs(root.left), 0)
            max_right_path = max(dfs(root.right), 0)
            current_max_path = max_left_path + max_right_path
            total = max(current_max_path + root.val, total)
            return root.val + max(max_left_path, max_right_path)

        dfs(root)
        return total
