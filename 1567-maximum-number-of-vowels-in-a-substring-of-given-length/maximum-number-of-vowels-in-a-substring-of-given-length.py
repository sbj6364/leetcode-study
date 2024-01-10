class Solution:
    vowels = ['a', 'e', 'i', 'o', 'u']

    def isVowel(self, c):
        if c in self.vowels:
            return True
        return False

    def countVowels(self, s):
        cnt = 0
        for c in s:
            if self.isVowel(c):
                cnt += 1
        return cnt

    def maxVowels(self, s: str, k: int) -> int:
        window = s[:k]
        max_v = self.countVowels(window)
        cnt_v = max_v
        for i in range(len(s) - k):
            if self.isVowel(s[i]):
                cnt_v -= 1
            if self.isVowel(s[i+k]):
                cnt_v += 1
            max_v = max(cnt_v, max_v)
        return max_v