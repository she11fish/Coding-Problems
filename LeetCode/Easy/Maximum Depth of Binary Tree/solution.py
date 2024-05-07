# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def ans(self, root, counter):
        if not root:
            return counter
        counter += 1
        left_counter = self.ans(root.left, counter)
        right_counter =  self.ans(root.right, counter)
        counter = max(left_counter, right_counter)
        return counter
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.ans(root, 0)
