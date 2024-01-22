class Solution:
    def decodeString(self, s: str) -> str:
        word = ""
        stack = []
        num = 0

        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c == "[":
                stack.append(num)
                stack.append(word)
                num = 0
                word = ""
            elif c == "]":
                prev_word = stack.pop()
                prev_num = stack.pop()
                word = prev_word + word * prev_num
            else:
                word += c

        while stack:
            word = stack.pop() + word
        
        return word
        