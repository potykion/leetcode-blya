from typing import List


class Solution:
    """
    https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

    >>> prices = [7,1,5,3,6,4]
    >>> Solution().maxProfit(prices)
    5
    >>> prices = [7,6,4,3,1]
    >>> Solution().maxProfit(prices)
    0
    >>> prices = [1]
    >>> Solution().maxProfit(prices)
    0
    >>> prices = [3,3]
    >>> Solution().maxProfit(prices)
    0
    >>> prices = [2,1,2,0,1]
    >>> Solution().maxProfit(prices)
    1
    """

    def maxProfit(self, prices: List[int]) -> int:
        def _step(prices):
            min_buy_price = 999_999
            min_buy_price_index = -1
            for index, price in enumerate(prices):
                if price < min_buy_price:
                    min_buy_price = price
                    min_buy_price_index = index

            return min_buy_price, min_buy_price_index

        max_profit = 0

        while True:
            if not prices:
                break
            min_buy_price, min_buy_price_index = _step(prices)
            max_profit = max(max_profit, max(prices[min_buy_price_index + 1:], default=0) - min_buy_price)
            prices = prices[:min_buy_price_index]

        return max_profit


# if __name__ == '__main__':
#     from src.utils import timeit
#     import json
#
#     # 0:00:00.133508
#     # 0:00:00.015624
#     with open("../data/6_1.json") as numbers_file:
#         timeit(Solution().maxProfit, json.load(numbers_file))
