class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        l = str(x)
        if l == l[::-1]:
            return True
        return False