class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        def collided(asteroid, last_item):
            return last_item > 0 and asteroid < 0            

        stack = []
        for asteroid in asteroids:
            while stack and collided(asteroid, stack[-1]):
                if abs(asteroid) == abs(stack[-1]):
                    stack.pop()
                    break
                if abs(asteroid) < abs(stack[-1]):
                    break
                stack.pop()
            else:
                stack.append(asteroid)
        return stack
