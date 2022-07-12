# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        #use deque() from import collections to make dbl ended queue
        dblQ = deque()
        
        dblQ.append(root)
        dblQ.append(root)
        
        while len(dblQ)>0:
            node1 = dblQ.popleft()
            node2 = dblQ.popleft()
            
            
            
            if node1 and not node2:
                return False
            
            if node2 and not node1:
                return False
            
            if not node1 and not node2:
                continue
                
            if node1.val != node2.val:
                return False
                
            dblQ.append(node1.right)
            dblQ.append(node2.left)
            dblQ.append(node1.left)
            dblQ.append(node2.right)
            
        return True
                
            
        
        
        
        
        
        