from datetime import datetime


def timeit(f, *args):
    """
    Usage:
    >>> s = Solution()
    >>> timeit(s.climbStairs, 35)
    """
    start = datetime.now()
    f(*args)
    print(datetime.now() - start)
