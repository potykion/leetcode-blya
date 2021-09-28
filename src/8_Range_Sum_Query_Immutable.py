from itertools import accumulate
from typing import List


class NumArray:
    """
    https://leetcode.com/problems/range-sum-query-immutable/

    >>> numArray = NumArray([-2, 0, 3, -5, 2, -1])
    >>> numArray.sumRange(0, 2)
    1
    >>> numArray.sumRange(2, 5)
    -1
    >>> numArray.sumRange(0, 5)
    -3
    """

    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        return sum(self.nums[left:right + 1])

    # https://www.youtube.com/watch?v=n_A2K_v7Sa8&list=PLyHj6yBbnkUgC6T9RpPxEBUv3My9lPd7m&index=9
    # def __init__(self, nums):
    #     self.sums = list(accumulate(nums))
    #
    # def sumRange(self, left: int, right: int) -> int:
    #     return (
    #         self.sums[right] - self.sums[left - 1]
    #         if left else
    #         self.sums[right]
    #     )
