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
