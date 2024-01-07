class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        for char in s:
            if len(t.split(char)) == 1: return False
            t = t[t.find(char)+1:]
        return True