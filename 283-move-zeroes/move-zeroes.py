class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        if 0 not in nums:
            return

        nums.sort(key=lambda x:x==0)


        """
        Do not return anything, modify nums in-place instead.
        """
        