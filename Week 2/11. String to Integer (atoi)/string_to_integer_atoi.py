class Solution:
    def myAtoi(self, s: str) -> int:
        pos_border = 2 ** 31 - 1
        neg_border = -2 ** 31
        minus = ''
        res = []
        i = 0
        while i < len(s) and s[i] == ' ':
            i += 1
        if i < len(s) and s[i] in ('+', '-'):
            if s[i] == '-':
                minus = '-'
            i += 1

        while i < len(s) and s[i] == '0':
            i += 1

        while i < len(s) and s[i].isdigit():
            res.append(s[i])
            i += 1
        res = int(minus + ''.join(res)) if res else 0

        if res <= neg_border:
            return neg_border
        if res >= pos_border:
            return pos_border
        return res