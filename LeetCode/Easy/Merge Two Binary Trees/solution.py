# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 and not root2:
            return
        root = TreeNode()
        def parallel(node1: Optional[TreeNode], node2: Optional[TreeNode], node: TreeNode) -> bool:
            if not node1 and not node2:
                return False
            node1_left = node1.left if node1 else None
            node1_right = node1.right if node1 else None
            node2_left = node2.left if node2 else None
            node2_right = node2.right if node2 else None
            if node1 and node2:
                node.val = node1.val + node2.val
            elif node1:
                node.val = node1.val
            elif node2:
                node.val = node2.val
            new = TreeNode()
            node.left = new
            ok1 = parallel(node1_left, node2_left, new)
            if not ok1:
                node.left = None
            new = TreeNode()
            node.right = new
            ok2 = parallel(node1_right, node2_right, new)
            if not ok2:
                node.right = None
            return True
        parallel(root1, root2, root)
        return root
