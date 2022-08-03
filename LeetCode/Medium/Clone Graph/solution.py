"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    
    def dfs_and_clone(self, node, new_node, existing_nodes, visited):
        if node in visited:
            return
        else:
            visited.add(node)
        new_neighbors = []

        # cloning algorithm
        for neighbor in node.neighbors:
            key = neighbor.val
            if key in existing_nodes:
                new_neighbors.append(existing_nodes[key])
            else:
                temp_node = Node(key)
                new_neighbors.append(temp_node)
                existing_nodes[key] = temp_node
        new_node.neighbors = new_neighbors

        for neighbor, new_neighbor in zip(node.neighbors, new_node.neighbors):
            self.dfs_and_clone(neighbor, new_neighbor, existing_nodes, visited)

            
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        if node:
            if not node.neighbors:
                return Node(node.val, [])
        visited = set()
        new_node = Node(node.val)
        existing_nodes = { new_node.val: new_node }
        self.dfs_and_clone(node, new_node, existing_nodes, visited)
        return new_node