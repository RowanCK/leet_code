package copy_list_with_random_pointer

// Definition for a Node.
type Node struct {
	Val    int
	Next   *Node
	Random *Node
}

func CopyRandomList(head *Node) *Node {
	existedNodes := make(map[*Node]*Node)
	newHead := deepCopy(&existedNodes, head)
	return newHead
}

func deepCopy(existedNodes *map[*Node]*Node, node *Node) *Node {
	if node == nil {
		return nil
	}

	if newNode, exists := (*existedNodes)[node]; exists {
		return newNode
	}

	newNode := &Node{Val: node.Val}
	(*existedNodes)[node] = newNode
	newNode.Next = deepCopy(existedNodes, node.Next)
	newNode.Random = deepCopy(existedNodes, node.Random)

	return newNode
}
