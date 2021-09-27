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
    >>> s.climbStairs(38)
    63245986
    """

    def climbStairs(self, n: int) -> int:
        cache = {1: 1, 2: 2}

        def _gen(n_):
            if n_ in cache:
                return cache[n_]
            else:
                return cache.setdefault(n_, _gen(n_ - 1) + _gen(n_ - 2))

        return _gen(n)
