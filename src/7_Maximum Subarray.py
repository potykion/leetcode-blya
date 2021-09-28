from typing import List


class Solution:
    """
    https://leetcode.com/problems/maximum-subarray/

    >>> s = Solution()
    >>> nums = [1,2,3]
    >>> s.maxSubArray(nums)
    6
    >>> nums = [-2,1,-3,4,-1,2,1,-5,4]
    >>> s.maxSubArray(nums)
    6
    >>> nums = [1]
    >>> s.maxSubArray(nums)
    1
    >>> nums = [5,4,-1,7,8]
    >>> s.maxSubArray(nums)
    23
    """

    def maxSubArray(self, nums: List[int]) -> int:
        arrays = (
            nums[inner:][:outer + 1]
            for inner in range(len(nums))
            for outer in range(len(nums[inner:]))
        )
        return max(map(sum, arrays))



if __name__ == '__main__':
    from src.utils import timeit
    import json

    with open("../data/7.json") as numbers_file:
        timeit(Solution().maxSubArray, json.load(numbers_file))
