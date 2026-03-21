# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None): # type: ignore
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None

        # Create interleaved copy nodes
        curr = head
        while curr:
            new_node = Node(curr.val, curr.next)
            curr.next = new_node
            curr = new_node.next

        # Assign random pointers to the copies
        curr = head
        while curr:
            if curr.random:
                # curr.next is the copy; curr.random.next is the copy of the random target
                curr.next.random = curr.random.next
            curr = curr.next.next

        # Separate the interweaved lists
        curr = head
        pseudo_head = Node(0) # Helper to track the start of the copy list
        copy_curr = pseudo_head

        while curr:
            # Link the copy list
            copy_curr.next = curr.next
            copy_curr = copy_curr.next

            # Restore the original list
            curr.next = copy_curr.next
            curr = curr.next

        return pseudo_head.next