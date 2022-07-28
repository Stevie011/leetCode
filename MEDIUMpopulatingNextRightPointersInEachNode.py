"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        #init pointers
        current, _next = root, root.left if root else None
        
        #stop if either of them become null
        while current and _next:
            #connect 'next' pointer of left node to right node
            current.left.next = current.right
            current.right.next = current.next.left if current.next else None
                
                
             #shift current node to next node in same level
            current = current.next
            if not current:
                current = _next
                _next = current.left
        return root


            