# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    total = 0
    def depth_traversal(self, root, stack, total):
        left = root.left
        right = root.right
        self.total += root.val
        if right != None:
            stack.append(right)
        if left != None:
            stack.append(left)
        if stack == []:
            return 
        self.depth_traversal(stack.pop(), stack, total)
    def solve(self, root):
        if not root:
            return 0
        stack = []
        self.depth_traversal(root, stack, self.total)    
        return self.total