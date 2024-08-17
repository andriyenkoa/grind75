import collections
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_letters = collections.Counter(p)
        cur_letters = collections.Counter(s[:len(p) - 1])

        res = []
        start = 0
        for i in range(len(p) - 1, len(s)):
            cur_letters[s[i]] += 1

            if cur_letters == p_letters:
                res.append(start)

            cur_letters[s[start]] -= 1
            if cur_letters[s[start]] == 0:
                del cur_letters[s[start]]

            start += 1

        return res
