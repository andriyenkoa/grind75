class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        checker = {}

        for one_char in s:
            if one_char in checker:
                checker[one_char] += 1
            else:
                checker[one_char] = 1

        for one_char in t:
            if one_char in checker:
                checker[one_char] -= 1
                if checker[one_char] < 0:
                    return False
            else:
                return False

        return sum(checker.values()) == 0


if __name__ == "__main__":
    solution = Solution()
    assert solution.isAnagram(s="anagram", t="nagaram") is True
    assert solution.isAnagram(s="rat", t="car") is False
