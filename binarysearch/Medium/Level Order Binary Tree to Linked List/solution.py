# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def create_linked_list(self, root, head):
        head.next = LLNode(root.val)
        head = head.next
        return head
        
    def bfs(self, root, queue, head):
        left = root.left
        right = root.right
        head = self.create_linked_list(root, head)
        if left:
            queue.insert(0, left)
        if right:
            queue.insert(0, right)
        if not queue:
            head.next = None
            return root
        self.bfs(queue.pop(), queue, head)
    
    def solve(self, root):
        queue = []
        head = LLNode(root.val)
        self.bfs(root, queue, head)
        head = head.next
        return head