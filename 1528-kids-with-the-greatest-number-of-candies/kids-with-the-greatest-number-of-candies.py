class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        n = len(candies)
        max_candies = max(candies)
        result = []

        for i in range(n):
            if candies[i] + extraCandies >= max_candies:
                result.append(True)
            else:
                result.append(False)

        return result
        