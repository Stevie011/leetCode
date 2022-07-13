# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #recursive dfs
            
        #give it the node, plus left and right boundaries
        def validator(node, left, right):
            #empty tree is still valid bst
            if not node: return True
            #check if node val is in between two pointers
            if not (node.val < right and node.val > left):
                return False
            #recursive call-- don't forget to keep call within function
            #check if left node is valid
            #since we're going left, keep left boundary the same, but update right boundary to node's val
            #for it to be valid, every val in subtree must be less than parent
            # swap it for right, coz both must be valid
            return (validator(node.left, left, node.val) and validator(node.right, node.val, right))
        #call the func, put in the root ofc, negative and postive infinity for pointers
        return validator(root, float("-inf"), float("inf"))
            
       
                
        