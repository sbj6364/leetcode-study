class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) == 1:
            return 1

        s = []
        cnt = 0

        for i in range(len(chars) - 1):
            if chars[i] == chars[i + 1]:
                cnt += 1
            else:
                s.append(chars[i])
                if cnt != 0:
                    s.append(str(cnt + 1))
                cnt = 0
        s.append(chars[-1])
        if cnt != 0:
            s.append(str(cnt + 1))
        s = list(''.join(s))

        chars.clear()
        for i in s:
            chars.append((i))

        return len(s)