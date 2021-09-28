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
        # https://www.youtube.com/watch?v=05MUgnQV_J8&list=PLyHj6yBbnkUgC6T9RpPxEBUv3My9lPd7m&index=5
        # mask = 0
        # for num in nums:
        #     mask ^= num
        # return mask

        return next((
            i
            for i, times in Counter(nums).items()
            if times == 1
        ))
