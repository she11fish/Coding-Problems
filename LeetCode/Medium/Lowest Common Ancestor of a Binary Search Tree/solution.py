# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    result = None
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def ans(root, p, q):
            if not root:
                return False
            left_bool = ans(root.left, p, q)
            right_bool = ans(root.right, p, q)
            
            target_exists = root == p or root == q

            if (left_bool and right_bool) or (left_bool and target_exists) or (right_bool and target_exists) and not self.result:   
                self.result = root 
                return True
            if target_exists:
                return True
            if left_bool or right_bool:
                return True
            return False
        ans(root, p, q)
        return self.result
