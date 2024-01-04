class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        tmp = 1
        
        for i in range(0, len(nums)):
            result.append(tmp)
            tmp = tmp * nums[i]
        
        tmp = 1
        for i in range(len(nums)-1, -1, -1):
            result[i] = result[i] * tmp
            tmp = tmp * nums[i]
        
        return result
        