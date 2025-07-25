# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        root = TreeNode(None)
        def helper(test: List[int], node: Optional[TreeNode]) -> None:
            if not test:
                return node
            middle = len(test) // 2
            node.val = test[middle]
            node.left = TreeNode(None)
            if helper(test[:middle], node.left).val is None:
                node.left = None
            node.right = TreeNode(None)
            if helper(test[middle + 1:], node.right).val is None:
                node.right = None 
            return node
        helper(nums, root)
        return root
