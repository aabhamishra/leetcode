
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


class Solution:
    def lowestCommonAncestor(self, p: Node, q: Node) -> Node:
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