class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = 'aeiouAEIOU'
        vowel_list = list(vowels)
        vowel_index = []
        str_vowels = []
        result = list(s)

        for i in range(len(s)):
            if s[i] in vowel_list:
                vowel_index.append(i)
                str_vowels.append(s[i])
        
        str_vowels.reverse()
    

        for i in range(len(vowel_index)):
            result[vowel_index[i]] = str_vowels[i]

        result = ''.join(result)

        return result
        