class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        l = 0
        r = len(skill) - 1
        skill.sort()
        total_skill = skill[0] + skill[-1]
        result = 0
        while l <= r:
            if skill[l] + skill[r] != total_skill:
                return -1
            result += skill[l] * skill[r]
            l += 1
            r -= 1
        return result
