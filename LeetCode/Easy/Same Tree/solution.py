# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    stack1 = []
    stack2 = []
    check = True
    
    def check_same_tree(self, right1, right2, left1, left2):
        # Check if right or left is none while the other is a valid node
        if (
                (not right1 and right2) \
                or (right1 and not right2) \
                or (not left1 and left2) \
                or (left1 and not left2)
        ): 
            return False
        if right1 and right2:
            return right1.val == right2.val
        if left1 and left2:
            return left1.val == left2.val
        return True
    
    def dfs(self, root1, root2):
        if root1:
            right1 = root1.right
            left1 = root1.left
        if root2:
            right2 = root2.right
            left2 = root2.left
        
        if right1:
            self.stack1.append(right1)
            test_right1 = right1
        elif right1:
            test_right1 = right1
        else:
            test_right1 = None  
            
        if left1:
            self.stack1.append(left1)
            test_left1 = left1
        elif left1:
            test_left1 = left1
        else:
            test_left1 = None
            
        if right2:
            self.stack2.append(right2)
            test_right2 = right2
        elif right2:
            test_right2 = right2
        else:
            test_right2 = None
            
        if left2:
            self.stack2.append(left2)
            test_left2 = left2
        elif left2:
            test_left2 = left2
        else:
            test_left2 = None
        if self.check:
            self.check = self.check_same_tree(test_right1, test_right2, test_left1, test_left2)
        
        if not self.stack1 or not self.stack2:
            return
        self.dfs(self.stack1.pop(), self.stack2.pop())
    
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Check if both are null
        if not p and not q:
            return True
        # Check if one of them is null
        elif (not p and q) or (p and not q):
            return False
        # Check if the root nodes are equal
        elif p.val != q.val:
            return False
        
        self.dfs(p, q)
        
        return self.check