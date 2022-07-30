# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    queue = []
    result = 0

    def breadth_first_traversal(self, root):
        right = root.right
        left = root.left
        self.result = root.val
        
        if right:
            self.queue.insert(0, right)
        if left:
            self.queue.insert(0, left)
        
        if self.queue == []:
            return 
        
        self.breadth_first_traversal(self.queue.pop())

    def solve(self, root):
        self.breadth_first_traversal(root)
        return self.result