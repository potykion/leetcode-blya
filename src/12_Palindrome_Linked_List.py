from typing import Optional

from src.utils import ListNode


class Solution:
    """
    https://leetcode.com/problems/palindrome-linked-list/

    >>> s = Solution()
    >>> s.isPalindrome(ListNode.from_list([1,2,2,1]))
    True
    """

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        nodes = []
        pos = head
        while pos:
            nodes.append(pos)
            pos = pos.next

        return [node.val for node in nodes] == [node.val for node in reversed(nodes)]

    # def isPalindrome(self, head: Optional[ListNode]) -> bool:
