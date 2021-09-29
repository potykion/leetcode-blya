from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes = []

        pos = head

        while True:
            nodes.append(pos)

            pos = pos.next
            if not pos:
                break

        return nodes[len(nodes) // 2]
