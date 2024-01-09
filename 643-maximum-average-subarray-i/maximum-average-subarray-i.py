class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        window = sum(nums[:k])
        max_ave = window/k

        if n == k:
            return max_ave

        for i in range(n - k):
            window = window - nums[i] + nums[i + k]
            max_ave = max(window/k, max_ave) 

        return max_ave
        