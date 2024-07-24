class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = {}
        result = 0
        for one_letter in s:
            if one_letter in counter:
                result += 2
                del counter[one_letter]
            else:
                counter[one_letter] = 1

        if len(counter) > 0:
            result += 1

        return result
