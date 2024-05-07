# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "null"
        queue = [root]
        result = []
        while len(queue):
            node = queue.pop()
            result.append("null" if (not node) else str(node.val))
            if not node:
                continue
            queue.insert(0, node.left)
            queue.insert(0, node.right)
        while result[-1] == "null":
            result.pop()
        return ", ".join(result)
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == "null" or data == "":
            return
        data = data.split(", ")
        head = TreeNode(None if data[0] == "    " else int(data[0]))
        queue = [head]
        left = 1
        right = 2
        while len(queue):
            start = queue.pop()
            print(start.val, left, right)
            if start.val == "null" or start.val == None:
                start.val = None
                continue
            if left < len(data):
                if data[left] != "null":
                    leftVal = int(data[left])
                    start.left = TreeNode(leftVal)
                    queue.insert(0, start.left)
                left += 2
            if right < len(data):
                if data[right] != "null":
                    rightVal = int(data[right])
                    start.right = TreeNode(rightVal)
                    queue.insert(0, start.right)
                right += 2
        return head
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
