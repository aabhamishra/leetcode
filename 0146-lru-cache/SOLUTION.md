## Intuition
The LRUCache class implements a Least Recently Used (LRU) Cache using a combination of a double linked list and a map. The linked list contains nodes representing key-value pairs, and the map contains a mapping of keys to their corresponding nodes.

## Approach

### `Node` Class

The inner `Node` class is used to represent a node in the linked list. Each node contains a key, value, and references to the previous and next nodes in the list.

### `__init__` Function
The constructor initializes the LRUCache with a specified capacity. It sets up the initial state of the cache, including the size, capacity, and the dummy head and tail nodes of the linked list.

### `add` Function
The add function is a helper method to add a new node to the front of the linked list. It updates the references of the adjacent nodes and adds the node to the map.

### `delete` Function
The delete function is a helper method to remove a node from the linked list. It updates the references of the adjacent nodes and removes the node from the map.

### `get` Function
The get function retrieves the value associated with a given key. If the key exists, it moves the corresponding node to the front of the list (indicating it was recently used). If the key does not exist, it returns -1.

### `put` Function
The put function inserts a new key-value pair into the cache. If the key already exists, it updates the value and moves the corresponding node to the front. If the key does not exist, it adds a new node to the front of the list. If the cache is at full capacity, it removes the least recently used item from the end of the list.

-x-x-x-

The LRUCache class efficiently manages a fixed-size cache, ensuring that the least recently used items are evicted when the cache is at full capacity. The combination of a linked list and a map provides quick access to nodes and efficient insertion and deletion operations.

## Complexity
- Time complexity: $O(1)$
The get and put functions take O(1) time thanks to the doubly linked list.

- Space complexity: $O(N)$
The HashMap tracks the number of key-value pairs that should be present in the LRU. As the cache is limited to `capacity`, the space taken is O(N) where `N = complexity`

## Code
```python
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
```