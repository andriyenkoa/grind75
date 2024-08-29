class Solution:
    def decodeString(self, s: str) -> str:
        num, idx, stack = 0, 0, [""]

        while idx < len(s):
            if s[idx].isdigit():
                num = 10*num + int(s[idx])
            elif s[idx] == "[":
                stack.append(num)
                stack.append("")
                num = 0
            elif s[idx] == "]":
                str1 = stack.pop()
                rep = stack.pop()
                str2 = stack.pop()
                stack.append(str2 + str1 * rep)
            else:
                stack[-1] += s[idx]
            idx += 1
        return stack.pop()
# stack = ["", 3, "a"]