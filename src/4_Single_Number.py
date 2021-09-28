from collections import Counter
from typing import List


class Solution:
    """
    https://leetcode.com/problems/single-number/

    >>> nums = [2,2,1]
    >>> Solution().singleNumber(nums)
    1
    >>> nums = [4,1,2,1,2]
    >>> Solution().singleNumber(nums)
    4
    >>> nums = [1]
    >>> Solution().singleNumber(nums)
    1
    """

    def singleNumber(self, nums: List[int]) -> int:
        return next((i for i, times in Counter(nums).items() if times == 1))
