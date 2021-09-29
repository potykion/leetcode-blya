from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     nodes = []
    #
    #     pos = head
    #
    #     while True:
    #         nodes.append(pos)
    #
    #         pos = pos.next
    #         if not pos:
    #             break
    #
    #     return nodes[len(nodes) // 2]

    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        slow = fast = head
        if not fast.next:
            return slow

        while True:
            slow = slow.next
            try:
                fast = fast.next.next
                if not fast.next:
                    break
            except AttributeError:
                break

        return slow
