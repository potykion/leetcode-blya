import json
from operator import itemgetter
from typing import List

from src.utils import timeit


class Solution:
    """
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
        max_profit = 0
        sorted_prices_with_index = sorted(enumerate(prices), key=itemgetter(1))
        for index, buy_price in sorted_prices_with_index:
            if index == len(prices) - 1:
                continue
            sell_price = max(prices[index+1:])

            max_profit = max(max_profit, sell_price - buy_price)

        return max_profit

if __name__ == '__main__':
    with open("../data/6.json") as numbers_file:
        timeit(Solution().maxProfit, json.load(numbers_file))