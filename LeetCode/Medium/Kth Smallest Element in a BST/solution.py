# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(root, res):
            if not root:
                return 
            left = dfs(root.left, res)
            right = dfs(root.right, res)
            if left != None:
                res.add(left)
            if right != None:
                res.add(right)
            return root.val
        res = set()
        res.add(root.val)
        dfs(root, res)
        ans = 1
        for k in range(k):
            if not res:
                return ans
            ans = min(res)
            res.remove(ans)
        return ans
