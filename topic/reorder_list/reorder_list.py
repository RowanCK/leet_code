# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head is None or head.next is None:
            return

        slow = fast = head
        while fast and fast.next:
            slow = slow.next # type: ignore
            fast = fast.next.next
        
        second_part = slow.next # type: ignore
        slow.next = None # type: ignore
        prev = None
        while second_part:
            next_node = second_part.next
            second_part.next = prev
            prev = second_part
            second_part = next_node
        
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
