from typing import Optional

# Definition for singly-linked list.
class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
		
        dummy = ListNode(0)
        dummy.next = head
        curr = head.next
        last_sorted = head

        while curr:
            if last_sorted.val <= curr.val: # type: ignore
                last_sorted = last_sorted.next # type: ignore
                curr = curr.next
            else:
                prev = dummy
                while prev.next and prev.next.val <= curr.val:
                    prev = prev.next
				
                last_sorted.next = curr.next # type: ignore
                curr.next = prev.next
                prev.next = curr
			
                curr = last_sorted.next # type: ignore

        return dummy.next
