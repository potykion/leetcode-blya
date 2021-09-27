from itertools import combinations
from typing import List


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
    """

    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        return max(0, max((c2 - c1 for c1, c2 in combinations(prices, 2))))
