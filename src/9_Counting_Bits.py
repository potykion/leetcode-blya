from typing import List


class Solution:
    """
    https://leetcode.com/problems/counting-bits/submissions/

    >>> s = Solution()
    >>> n = 2
    >>> s.countBits(n)
    [0, 1, 1]
    >>> n = 5
    >>> s.countBits(n)
    [0, 1, 1, 2, 1, 2]
    """

    def countBits(self, n: int) -> List[int]:
        return [
            sum(map(int, "{:b}".format(i)))
            for i in range(n + 1)
        ]
