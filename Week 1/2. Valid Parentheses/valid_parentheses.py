class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        checker = {
            "(": ")",
            "[": "]",
            "{": "}"
        }

        for one_bracket in s:
            if one_bracket in checker.keys():
                stack.append(checker[one_bracket])
            else:
                if stack and stack[-1] == one_bracket:
                    stack.pop()
                else:
                    return False

        return len(stack) == 0


if __name__ == "__main__":
    solution = Solution()
    assert solution.isValid(s="()") is True
    assert solution.isValid(s="()[]{}") is True
    assert solution.isValid(s="(]") is False
