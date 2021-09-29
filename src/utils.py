from datetime import datetime
from itertools import islice


def timeit(f, *args):
    """
    Usage:
    >>> s = Solution()
    >>> timeit(s.climbStairs, 35)
    """
    start = datetime.now()
    f(*args)
    print(datetime.now() - start)


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @classmethod
    def from_list(cls, list_):
        prev_node = ListNode(val=list_[-1])
        for item in islice(reversed(list_), 1):
            node = ListNode(val=item, next=prev_node)
            prev_node = node

        return node
