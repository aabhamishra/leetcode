## Intuition
If the input nodes `p` and `q` are guaranteed to have an ancestor, we know that at some point swimming up from the nodes to root, we will encounter the ancestor. We basically need to track all ancestors of each node we encounter, and return as soon as a node is an ancestor of both input nodes.

To track efficiently and as the order does not metter, we use a set. 

## Approach

The algorithm uses a set to keep track of the ancestors of both nodes `p` and `q`. It iterates through the ancestors by moving up the tree using the parent pointers until a common ancestor is found.

1. **Set of Ancestors**: Initialize an empty set called `ancestors` to keep track of the ancestors of nodes.
2. **Iterative Traversal**: While either of the nodes `p` or `q` is not null:
    - For node `p`:
        - If `p` is already in the set of ancestors, return `p` as it is the lowest common ancestor.
        - Else, add `p` to the set of ancestors.
        - Move to the parent of `p`.
    - For node `q`:
        - If `q` is already in the set of ancestors, return `q` as it is the lowest common ancestor.
        - Add `q` to the set of ancestors.
        - Move to the parent of `q`.
3. **Return Dummy Node**: If no common ancestor is found, return a dummy node (e.g., `Node(0)`). This will never happen as we are guaranteed to find an LCA of both nodes according to the question. 

## Complexity
- Time complexity: $O(H)$
The time complexity is O(H), where H is the height of the binary tree. In the worst case, the algorithm traverses the height of the tree.


- Space complexity: $O(H)$
The space complexity is O(H), where H is the height of the binary tree. The set of ancestors stores at most H nodes.

## Code
```python
"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        ancestors = set()

        while(p or q):
            if p:
                if p in ancestors:
                    return p
                ancestors.add(p)
                p = p.parent

            if q:
                if q in ancestors:
                    return q
                ancestors.add(q)
                q = q.parent
    
        return Node(0)
```