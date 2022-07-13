# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        #hashmap approach
        #x + y = k
        #therefore
        # y = k-x
        
        lookup = set()
        def dfs(node):
            if not node: return False
            #as per earlier maffs
            y = k - node.val
            #if we can match the y val, return True
            if y in lookup: 
                return True
            else:
                #add node.val to lookup
                lookup.add(node.val)
            # if either side can return true then the whole thing is true
            return dfs(node.left) or dfs(node.right)
        #call the func, plug in root, return true/false
        return dfs(root)
                
            
        