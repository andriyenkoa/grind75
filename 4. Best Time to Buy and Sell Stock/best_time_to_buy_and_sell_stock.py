from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        price_to_buy = prices[0]

        for price in prices:
            if price < price_to_buy:
                price_to_buy = price
            else:
                cur_profit = price - price_to_buy
                max_profit = max(max_profit, cur_profit)

        return max_profit


if __name__ == "__main__":
    solution = Solution()
    assert solution.maxProfit(prices=[7, 1, 5, 3, 6, 4]) == 5
    assert solution.maxProfit(prices=[7, 6, 4, 3, 1]) == 0
