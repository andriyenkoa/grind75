from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for one_str in strs:
            sorted_one_str = str(sorted(one_str))
            if sorted_one_str in res:
                res[sorted_one_str].append(one_str)
            else:
                res[sorted_one_str] = [one_str]
        return list(res.values())
