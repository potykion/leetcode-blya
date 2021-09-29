from collections import Counter


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
    https://leetcode.com/problems/linked-list-cycle/

    """

    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False

        pointer = head
        counter = Counter()

        while True:
            counter[pointer] += 1

            if counter[pointer] > 1:
                return True

            pointer = pointer.next
            if not pointer:
                break

        return False

        # https://www.youtube.com/watch?v=k2DP9Gd13F4&list=PLyHj6yBbnkUgC6T9RpPxEBUv3My9lPd7m&index=11
        # if not head:
        #     return False
        #
        # slow = fast = head
        #
        # while fast.next and fast.next.next:
        #     fast = fast.next.next
        #     slow = slow.next
        #
        #     if fast == slow:
        #         return True
        #
        # return False
