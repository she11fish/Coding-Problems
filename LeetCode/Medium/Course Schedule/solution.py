class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(og_root, root, graph, visited):
            if root in visited and og_root == root:
                return False
            if root in visited:
                return True
            if not root in graph:
                return True
            visited.add(root)
            boolean = True
            for neighbour in graph[root]:
                boolean = dfs(og_root, neighbour, graph, visited) and True
                if not boolean:
                    return False
            return True
        graph = {}
        for course1, course2 in prerequisites:
            if not course2 in graph:
                graph[course2] = []
            graph[course2].append(course1)
        for node in graph:
            if not dfs(node, node, graph, set()):
                return False
        return True
