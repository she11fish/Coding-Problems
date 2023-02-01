# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def maximum(root):
            if not root:
                return float('-inf')
            return max(max(maximum(root.right), root.val), max(maximum(root.left), root.val))
        def minimum(root):
            if not root:
                return float('inf')
            return min(min(minimum(root.right), root.val), min(minimum(root.left), root.val))
        if not root:
            return False
        stack = [root]
        while stack:
            curr = stack.pop()
            if curr.left:
                if curr.left.val < curr.val and maximum(curr.left) < curr.val:
                    print(maximum(curr.left))
                    stack.append(curr.left)
                else:
                    return False
            if curr.right:
                if curr.right.val > curr.val and minimum(curr.right) > curr.val:
                    print(minimum(curr.left))
                    stack.append(curr.right)
                else:
                    return False
        return True
