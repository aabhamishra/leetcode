class LRUCache:
    # double linked list with map
    # linked list contains nodes, map contains key -> Node
    class Node:
        def __init__(self, key, val):
            self.key = key
            self.val = val

            self.prev = None
            self.next = None
    
    def __init__(self, capacity: int):
        self.size = 0
        self.cap = capacity

        self.head = self.Node(-1, -1)
        self.tail = self.Node(-1, -1)

        self.head.next = self.tail
        self.tail.prev = self.head

        self.map = {}
    
    def add(self, node: Node):
        next = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = next
        next.prev = node
        self.map[node.key] = node

    def delete(self, node: Node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p
        self.map.pop(node.key)

    def get(self, key: int) -> int:
        if key in self.map:
            curr = self.map[key]
            self.delete(curr)
            self.add(curr)
            return curr.val     
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.delete(self.map[key])
            self.size-=1

        if self.size == self.cap:
            self.delete(self.tail.prev)
            self.size-=1     

        curr = self.Node(key,value)
        self.add(curr)
        self.size+=1 

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)