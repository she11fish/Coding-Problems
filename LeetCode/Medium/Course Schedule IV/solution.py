class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = {}
        for prereq, course in prerequisites:
            if prereq not in graph:
                graph[prereq] = [course]
            else:
                graph[prereq].append(course)
        memo = {}
        def dfs(root):
            if root in memo:
                return memo[root]
            memo[root] = set()
            for neighbor in graph[root]:
                memo[root] |= dfs(neighbor)
                memo[root].add(neighbor)
            return memo[root]
        for i in range(numCourses):
            if i not in graph:
                graph[i] = []
        for i in range(numCourses):
            dfs(i)
        res = []
        for query in queries:
            res.append(query[1] in memo[query[0]])
        return res