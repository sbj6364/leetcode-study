class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        maxlen = max(len(word1), len(word2))
        result = ""

        for i in range(maxlen):
            try:
                char = word1[i]
                result = result+char
            except: pass
            try:
                char = word2[i]
                result = result+char
            except: pass

        return result        
