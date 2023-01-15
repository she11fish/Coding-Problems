class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(root, counter, maximum):
            if not root:
                return counter + 1
            left_count = dfs(root.left, counter, maximum)
            right_count =  dfs(root.right, counter, maximum)
            maximum[0] = max(left_count + right_count, maximum[0])
            return max(left_count, right_count) + 1  
        maximum = [0]
        dfs(root, -1, maximum)
        return maximum[0]
