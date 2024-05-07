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
    
    def linked_list(self, result):
        root = LLNode(result[0])
        next_node = root
        for i in range(1, len(result)):
            next_node.next = LLNode(result[i])
            next_node = next_node.next
        next_node.next = None
        return root

    def inorder_traversal(self, root, result):
        if not root:
            return

        left = root.left
        right = root.right
        
        self.inorder_traversal(left, result)

        result.append(root.val)

        self.inorder_traversal(right, result)


    def solve(self, root):
        if not root:
            return root
        result = []
        self.inorder_traversal(root, result)
        answer = self.linked_list(result)
        return answer