class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        checker = {}
        max_val = 0
        i = 0

        for j in range(len(s)):
            if s[j] in checker:
                max_val = max(max_val, j - i)
                i = max(i, checker[s[j]] + 1)
            checker[s[j]] = j

        max_val = max(max_val, len(s) - i)
        return max_val
