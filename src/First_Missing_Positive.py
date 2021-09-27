from typing import List


class Solution:
    """
    https://leetcode.com/problems/first-missing-positive/submissions/
    """

    def firstMissingPositive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        for i in range(1, len(nums) + 1):
            if i not in nums_set:
                return i

        return len(nums) + 1
