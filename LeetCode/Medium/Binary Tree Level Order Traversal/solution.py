# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    queue = []  

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def bfs(root, result):
            if not root:
                return
            layer = 1
            self.queue.append((root, layer))
            result.append([root.val])
            while len(self.queue):
                curr, layer = self.queue.pop()
                print(layer, curr.val)
                if curr.left:
                    if layer >= len(result):
                        result.append([curr.left.val])
                    else:
                        result[layer].append(curr.left.val)
                    self.queue.insert(0, (curr.left, layer + 1))
                if curr.right:
                    if layer >= len(result):
                        result.append([curr.right.val])
                    else:
                        result[layer].append(curr.right.val)
                    self.queue.insert(0, (curr.right, layer + 1))
        result = []
        bfs(root, result)
        return result
