class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left = 0
        right = sum(nums) - nums[0]

        for i in range(len(nums)):
            if left == right:
                return i
            else:
                left += nums[i]
                if i < len(nums) - 1:
                    right -= nums[i + 1]
        return -1

        