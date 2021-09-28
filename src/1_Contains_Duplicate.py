from typing import List


class Solution:
    """
    https://leetcode.com/problems/contains-duplicate/submissions/

    >>> nums = [1,2,3,1]
    >>> Solution().containsDuplicate(nums)
    True
    >>> nums = [1,2,3,4]
    >>> Solution().containsDuplicate(nums)
    False
    >>> nums = [1,1,1,3,3,4,3,2,4,2]
    >>> Solution().containsDuplicate(nums)
    True
    """

    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
