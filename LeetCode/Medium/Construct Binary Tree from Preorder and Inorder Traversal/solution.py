# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return
        i = 0
        while i < len(preorder) and preorder[i] not in inorder:
            i += 1
        if i == len(preorder):
            return
        tree = TreeNode(preorder[i])
        pivot_index = inorder.index(preorder[i])
        tree.left = self.buildTree(preorder[:i] + preorder[i + 1:], inorder[:pivot_index])
        tree.right = self.buildTree(preorder[:i] + preorder[i + 1:], inorder[pivot_index + 1:])
        return tree
