class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        nums = list(set(arr))
        prev_cnt = []
        for num in nums:
            cnt = arr.count(num)
            if cnt in prev_cnt:
                return False
            prev_cnt.append(cnt)
        
        return True