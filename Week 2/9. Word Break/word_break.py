from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}

        def helper(length):
            if length == len(s):
                return True
            if length in memo:
                return memo[length]

            for word in wordDict:
                if s[length:].startswith(word):
                    if helper(length + len(word)):
                        memo[length] = True
                        return True
            memo[length] = False
            return False

        return helper(0)
