class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        return self.counter(n, memo)

    def counter(self, n: int, memo: dict[int, int]) -> int:
        if n == 0 or n == 1:
            return 1
        if n not in memo:
            memo[n] = self.counter(n - 1, memo) + self.counter(n - 2, memo)

        return memo[n]

    def climbStairs2(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        prev, curr = 1, 1
        for i in range(2, n + 1):
            temp = curr
            curr = prev + curr
            prev = temp
        return curr
