# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        temp = []
        def traverse(node: Optional[TreeNode]) -> None:
            if node is None:
                return node
            left = traverse(node.left)
            temp.append(node.val)
            right = traverse(node.right)
        traverse(root)
        return temp
