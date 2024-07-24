class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter = {}

        for one_letter in magazine:
            if one_letter in counter:
                counter[one_letter] += 1
            else:
                counter[one_letter] = 1

        for one_letter in ransomNote:
            if one_letter not in counter or counter[one_letter] < 1:
                return False
            counter[one_letter] -= 1

        return True
