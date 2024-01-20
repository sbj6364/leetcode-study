class Solution:
    def removeStars(self, s: str) -> str:
        result = []
        i = len(s) - 1
        stars = 0
        while i >= 0:
            if s[i] == '*':
                stars += 1
            elif stars > 0:
                stars -= 1
            elif i >= 0:
                result.append(s[i])
            i -= 1
        
        return ''.join(result[::-1])

        