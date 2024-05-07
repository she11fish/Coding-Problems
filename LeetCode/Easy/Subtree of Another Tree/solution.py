# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check_subRoot(self, root, subRoot):
        if not root and not subRoot:
            return True
        if (not root and subRoot) or (root and not subRoot):
            return False
        if root.val != subRoot.val:
            return False
        return self.check_subRoot(root.left, subRoot.left) and self.check_subRoot(root.right, subRoot.right)
    def dfs(self, root, subRoot):
        if not root:
            return False
        isSubRoot = False
        if root.val == subRoot.val:
            isSubRoot = self.check_subRoot(root, subRoot)
        return self.dfs(root.left, subRoot) or self.dfs(root.right, subRoot) or isSubRoot
    def subRootHead_exists(self, root, subRoot):
        if not root:
            return False
        if root.val == subRoot.val:
            return True
        return self.subRootHead_exists(root.left, subRoot) or self.subRootHead_exists(root.right, subRoot)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if not self.subRootHead_exists(root, subRoot):
            return False
        return self.dfs(root, subRoot)
