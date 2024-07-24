class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            if not s[left].isalnum():
                left += 1
                continue
            if not s[right].isalnum():
                right -= 1
                continue

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True

    # Faster, but I don't like many (left < right) checks => readability is low imo
    def isPalindrome2(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1

            if left < right and s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True


if __name__ == "__main__":
    solution = Solution()
    assert solution.isPalindrome(s="A man, a plan, a canal: Panama") is True
    assert solution.isPalindrome(s="race a car") is False
    assert solution.isPalindrome(s=" ") is True
