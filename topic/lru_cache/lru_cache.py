from typing import Dict, Optional

class Node:
	def __init__(self, key: int, value: int):
		self.key: int = key
		self.value: int = value
		self.prev: Optional[Node] = None
		self.next: Optional[Node] = None

class LRUCache:
	def __init__(self, capacity: int):
		self.capacity: int = capacity
		self.cache: Dict[int, Node] = {}
		self.head: Node = Node(0, 0)
		self.tail: Node = Node(0, 0)
		self.head.next = self.tail
		self.tail.prev = self.head
		return None

	def get(self, key: int) -> int:
		if key in self.cache:
			node = self.cache[key]
			self.remove(node)
			self.add(node)
			return node.value
		return -1

	def put(self, key: int, value: int) -> None:
		if key in self.cache:
			self.remove(self.cache[key])
		elif len(self.cache) == self.capacity:
			lru_node = self.head.next
			assert lru_node is not None
			self.remove(lru_node)
			del self.cache[lru_node.key]

		new_node = Node(key, value)
		self.cache[key] = new_node
		self.add(new_node)

	def add(self, node: Node) -> None:
		last_node = self.tail.prev
		assert last_node is not None

		node.prev = last_node
		node.next = self.tail
		last_node.next = node
		self.tail.prev = node

	def remove(self, node: Node) -> None:
		if node.prev:
			node.prev.next = node.next
		if node.next:
			node.next.prev = node.prev

capacity = 10
key = 1
value = 2

obj = LRUCache(capacity)
param_1 = obj.get(key)
obj.put(key,value)