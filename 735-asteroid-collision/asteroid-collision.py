class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        result = []

        for asteroid in asteroids:
            if not result or asteroid > 0:
                result.append(asteroid)
            else:
                while True:
                    top = result[-1]
                    if top < 0:
                        result.append(asteroid)
                        break
                    elif top == -asteroid:
                        result.pop()
                        break
                    elif top > -asteroid:
                        break
                    else:
                        result.pop()
                        if not result:
                            result.append(asteroid)
                            break
        
        return result
        