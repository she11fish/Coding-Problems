# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root.left and not root.right:
            return root.val
        def dfs(root, total):
            if not root:
                return total
            result = max(dfs(root.left, total + root.val), dfs(root.right, total + root.val), total)
            return result

        stack = []
        stack.append(root)
        maximum = float("-inf")
        while len(stack):
            currentNode = stack.pop()
            if currentNode.left and currentNode.right:
                max_left_path = dfs(currentNode.left, 0)
                max_right_path = dfs(currentNode.right, 0)
                total = 0
                if max_left_path >= 0:
                    total += max_left_path
                if max_right_path >= 0:
                    total += max_right_path
                total += currentNode.val
                print(max_left_path, max_right_path)
                maximum = max(maximum, total)
                stack.append(currentNode.left)
                stack.append(currentNode.right)
            elif currentNode.left:
                max_left_path = dfs(currentNode.left, 0)
                total = 0
                if max_left_path >= 0:
                    total += max_left_path
                total += currentNode.val
                maximum = max(maximum, total)
                stack.append(currentNode.left)
            elif currentNode.right:
                max_right_path = dfs(currentNode.right, 0)
                total = 0
                if max_right_path >= 0:
                    total += max_right_path
                total += currentNode.val
                maximum = max(maximum, total)
                stack.append(currentNode.right)
            else:
                maximum = max(maximum, currentNode.val)
        return maximum
