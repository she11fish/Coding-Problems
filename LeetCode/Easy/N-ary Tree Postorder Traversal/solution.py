"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        temp = []
        def traverse(node: Node) -> None:
            if node is None or node.val is None:
                return
            if node.children is None:
                temp.append(node.val)
                return
            for child in node.children:
                traverse(child)
            temp.append(node.val)
        traverse(root)
        return temp
