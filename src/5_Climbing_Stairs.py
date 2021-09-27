class Solution:
    """
    >>> s = Solution()
    >>> s.climbStairs(1)
    1
    >>> s.climbStairs(2)
    2
    >>> s.climbStairs(3)
    3
    >>> s.climbStairs(4)
    5
    >>> s.climbStairs(5)
    8
    >>> s.climbStairs(6)
    13
    >>> s.climbStairs(35)
    14930352
    """

    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)
