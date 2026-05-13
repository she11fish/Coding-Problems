class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if not prerequisites:
            return list(range(numCourses))
        d = {}
        for i in range(len(prerequisites)):
            if prerequisites[i][1] not in d:
                d[prerequisites[i][1]] = [prerequisites[i][0]]
            else:
                d[prerequisites[i][1]].append(prerequisites[i][0])
            if prerequisites[i][0] not in d:
                d[prerequisites[i][0]] = []
        for i in range(numCourses):
            if i not in d:
                d[i] = []
        seen = set()

        def find_best_choice(item, visited):
            if item in seen:
                return []
            if item in visited:
                return None
            if d[item] == []:
                return [item]
            t = []
            visited.add(item)
            for e in d[item]:
                a = find_best_choice(e, visited)
                if a is None:
                    return None
                t.extend(a)
            visited.remove(item)
            seen.add(item)
            return t

        r = set()
        for i in range(numCourses):
            t = find_best_choice(i, set())
            if t is None:
                return []
            for e in t:
                r.add(e)
        r = list(r)
        d = {}
        for i in range(len(prerequisites)):
            if prerequisites[i][0] not in d:
                d[prerequisites[i][0]] = [prerequisites[i][1]]
            else:
                d[prerequisites[i][0]].append(prerequisites[i][1])
            if prerequisites[i][1] not in d:
                d[prerequisites[i][1]] = []
        for i in range(numCourses):
            if i not in d:
                d[i] = []

        v = set()

        def dfs(item):
            if item in v:
                return []
            v.add(item)
            if d[item] == []:
                return [item]
            res = []
            for e in d[item]:
                res.extend(dfs(e))
            res.append(item)
            return res

        res = []
        for num in r:
            res.extend(dfs(num))
        return res
