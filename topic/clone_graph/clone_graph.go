package clone_graph

type Node struct {
	Val       int
	Neighbors []*Node
}

func CloneGraph(node *Node) *Node {
	if node == nil {
		return nil
	}

	cloned := make(map[*Node]*Node)

	var dfs func(n *Node) *Node
	dfs = func(n *Node) *Node {
		if n == nil {
			return nil
		}

		if clone, ok := cloned[n]; ok {
			return clone
		}

		clone := &Node{Val: n.Val}
		cloned[n] = clone

		for _, neighbor := range n.Neighbors {
			clone.Neighbors = append(clone.Neighbors, dfs(neighbor))
		}

		return clone
	}

	return dfs(node)
}

func CloneGraph_bfs(node *Node) *Node {
	if node == nil {
		return nil
	}

	cloned := make(map[*Node]*Node)
	queue := []*Node{node}
	cloned[node] = &Node{Val: node.Val}

	for len(queue) > 0 {
		curr := queue[0]
		queue = queue[1:]

		for _, neighbor := range curr.Neighbors {
			if _, ok := cloned[neighbor]; !ok {
				cloned[neighbor] = &Node{Val: neighbor.Val}
				queue = append(queue, neighbor)
			}
			cloned[curr].Neighbors = append(cloned[curr].Neighbors, cloned[neighbor])
		}
	}

	return cloned[node]
}
