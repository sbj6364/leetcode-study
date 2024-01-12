class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for i in range(0, len(nums)):
            left = sum(nums[:i])
            right = sum(nums[i+1:])

            if left - right == 0:
                return i
        
        return -1

        