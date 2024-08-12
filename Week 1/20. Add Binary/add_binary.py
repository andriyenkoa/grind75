class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j = len(a) - 1, len(b) - 1
        result = ""
        carry = 0
        while i >= 0 or j >= 0:
            sum = carry

            if i >= 0:
                sum += ord(a[i]) - ord('0')
            if j >= 0:
                sum += ord(b[j]) - ord('0')
            i -= 1
            j -= 1

            carry = 1 if sum > 1 else 0
            result += str(sum % 2)

        if carry == 1:
            result += "1"

        return result[::-1]




solution = Solution()
print(solution.addBinary('100', '101'))
