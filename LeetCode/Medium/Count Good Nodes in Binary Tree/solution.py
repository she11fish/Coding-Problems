# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
            if not root:
                return 0
            stack = [(root, root.val)]
            maximum = root.val
            counter = 1
            while stack:
                curr, maximum = stack.pop()
                if curr.left:
                    if maximum <= curr.left.val:
                        counter += 1
                    stack.append((curr.left, max(maximum, curr.left.val)))
                if curr.right:
                    if maximum <= curr.right.val:
                        counter += 1
                    stack.append((curr.right, max(maximum, curr.right.val)))
            return counter
                
