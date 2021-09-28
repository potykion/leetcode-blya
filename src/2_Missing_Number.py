from typing import List


class Solution:
    """
    https://leetcode.com/problems/missing-number/

    >>> nums = [3,0,1]
    >>> Solution().missingNumber(nums)
    2
    >>> nums = [0,1]
    >>> Solution().missingNumber(nums)
    2
    >>> nums = [9,6,4,2,3,5,7,0,1]
    >>> Solution().missingNumber(nums)
    8
    >>> nums = [0]
    >>> Solution().missingNumber(nums)
    1
    """

    def missingNumber(self, nums: List[int]) -> int:
        return sum(range(len(nums) + 1)) - sum(nums)
