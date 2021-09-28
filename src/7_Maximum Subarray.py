from collections import deque
from typing import List


class Solution:
    """
    https://leetcode.com/problems/maximum-subarray/

    >>> s = Solution()
    >>> nums = [3,2,-3,-1,1,-3,1,-1]
    >>> s.maxSubArray(nums)
    5
    >>> nums = [-1,-2,3,-1,-2,1,1]
    >>> s.maxSubArray(nums)
    3
    >>> nums = [-1,1,-1,2,-2,-2]
    >>> s.maxSubArray(nums)
    2
    >>> nums = [1,1,-2]
    >>> s.maxSubArray(nums)
    2
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
    >>> nums = [-1]
    >>> s.maxSubArray(nums)
    -1

    """

    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = sum(nums)
        result = nums
        while True:
            deque_ = deque(result)
            buffer = []
            sum_acc = 0
            while deque_:
                el = deque_.popleft()
                buffer.append(el)
                sum_acc += el
                max_sum = max(max_sum, sum_acc)
                if sum_acc < 0:
                    sum_acc = 0
                    buffer = []
            result = buffer or nums

            deque_ = deque(result)
            buffer = []
            sum_acc = 0
            while deque_:
                el = deque_.pop()
                buffer.append(el)
                sum_acc += el
                max_sum = max(max_sum, sum_acc)
                if sum_acc < 0:
                    sum_acc = 0
                    buffer = []
            new_result = buffer[::-1]
            if not new_result:
                result = new_result
                break

            if len(result) == len(new_result):
                result = new_result
                break
            else:
                result = new_result

        return max(filter(None, [max_sum, sum(result), max(nums)]), default=0)

        # # https://www.youtube.com/watch?v=vDlxW-_QEpI&list=PLyHj6yBbnkUgC6T9RpPxEBUv3My9lPd7m&index=8
        # max_sum = cur_sum = nums[0]
        #
        # for num in nums[1:]:
        #     cur_sum = max(cur_sum + num, num)
        #     max_sum = max(cur_sum, max_sum)
        #
        # return max_sum

# if __name__ == '__main__':
#     from src.utils import timeit
#     import json
#
#     with open("../data/7_1.json") as numbers_file:
#         # 0:00:12.843720
#         # 0:00:08.843720
#         # 0:00:06.338794
#         # 0:00:00.023174
#         timeit(Solution().maxSubArray, json.load(numbers_file))
