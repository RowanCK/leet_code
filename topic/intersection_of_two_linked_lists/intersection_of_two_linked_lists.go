package increasing_triplet_subsequence

// Definition for singly-linked list.
type ListNode struct {
	Val  int
	Next *ListNode
}

func GetIntersectionNode(headA, headB *ListNode) *ListNode {
	a := headA
	b := headB

	for a != b {
		if a == nil {
			a = headB
		} else {
			a = a.Next
		}

		if b == nil {
			b = headA
		} else {
			b = b.Next
		}
	}

	return a
}

func GetIntersectionNode2(headA, headB *ListNode) *ListNode {
	visited := make(map[*ListNode]struct{})

	for curr := headA; curr != nil; curr = curr.Next {
		visited[curr] = struct{}{}
	}

	for curr := headB; curr != nil; curr = curr.Next {
		if _, exists := visited[curr]; exists {
			return curr
		}
	}

	return nil
}
