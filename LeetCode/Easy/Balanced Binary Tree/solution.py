# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, counter, truthiness):
            if not root:
                return counter + 1
            left_count = dfs(root.left, counter, truthiness)
            right_count = dfs(root.right, counter, truthiness)
            if abs(left_count - right_count) > 1:
                truthiness[0] = False
            return max(left_count, right_count) + 1
        truthiness = [True]
        dfs(root, -1, truthiness)
        return truthiness[0]
