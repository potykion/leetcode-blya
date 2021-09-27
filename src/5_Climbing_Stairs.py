class Solution:
    """
    >>> s = Solution()
    >>> s.climbStairs(2)
    2
    >>> s.climbStairs(3)
    3
    >>> s.climbStairs(4)
    5
    >>> s.climbStairs(5)
    8
    """

    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1

        def get_way(way, n):
            way_sum = sum(way)

            if way_sum > n:
                return

            if way_sum == n:
                yield way
                return

            yield from get_way(way + [1], n)
            yield from get_way(way + [2], n)

        return len([*get_way([1], n), *get_way([2], n)])
