class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        d = {-1: 0}
        for row in wall:
            prefix = 0

            for brick in row[:-1]:
                prefix += brick
                if prefix not in d:
                    d[prefix] = 1
                else:
                    d[prefix] += 1
        return len(wall) - max(d.values())
