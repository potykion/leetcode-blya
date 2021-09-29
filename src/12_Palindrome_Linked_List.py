# Definition for singly-linked list.
from operator import itemgetter
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    https://leetcode.com/problems/palindrome-linked-list/

    >>> s = Solution()
    >>> s.isPalindrome(ListNode(1, next=ListNode(2, next=ListNode(2, next=ListNode(1)))))
    True
    """

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        nodes = []
        pos = head
        while pos:
            nodes.append(pos)
            pos = pos.next

        return [node.val for node in nodes] == [node.val for node in reversed(nodes)]
