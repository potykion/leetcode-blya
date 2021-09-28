from typing import List


class Solution:
    """
    https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

    >>> nums = [4,3,2,7,8,2,3,1]
    >>> Solution().findDisappearedNumbers(nums)
    [5, 6]
    >>> nums = [1,1]
    >>> Solution().findDisappearedNumbers(nums)
    [2]
    """

    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        all_numbers = {i for i in range(1, len(nums) + 1)}
        for num in nums:
            try:
                all_numbers.remove(num)
            except KeyError:
                pass
        return list(all_numbers)
