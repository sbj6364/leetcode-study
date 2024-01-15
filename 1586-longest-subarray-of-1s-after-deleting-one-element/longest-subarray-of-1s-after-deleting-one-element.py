class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        maxone = 0
        z = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                z += 1

            while z > 1:
                if nums[left] == 0:
                    z -= 1
                left += 1

            maxone = max(maxone, right - left)
        
        return maxone


