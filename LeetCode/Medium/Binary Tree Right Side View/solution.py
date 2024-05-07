# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = []
        def bfs(root, result):
            if not root:
                return
            result.append(root.val)
            layer = 1
            queue.append((root, layer))
            while queue:
                curr, layer = queue.pop(0)
                if curr.right:
                    if layer >= len(result):
                        result.append(curr.right.val)
                    queue.append((curr.right, layer + 1))
                if curr.left:    
                    if layer >= len(result):
                        result.append(curr.left.val)
                    queue.append((curr.left, layer + 1))
        result = []
        bfs(root, result)
        return result
