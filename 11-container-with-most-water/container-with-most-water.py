class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_container = 0
        l = 0
        r = len(height) - 1

        while l < r:
            lh = height[l]
            rh = height[r]
            smaller_h = min(lh, rh)
            container = smaller_h * (r - l)
            max_container = max(max_container, container)

            if lh < rh:
                l += 1
            else:
                r -= 1

        return max_container