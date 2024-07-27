from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in ('+', '-', '*', '/'):
                second_num = stack.pop()
                first_num = stack.pop()
                if token == '+':
                    stack.append(first_num + second_num)
                elif token == '-':
                    stack.append(first_num - second_num)
                elif token == '*':
                    stack.append(first_num * second_num)
                elif token == '/':
                    stack.append(int(first_num / second_num))
            else:
                stack.append(int(token))
        return stack.pop()
