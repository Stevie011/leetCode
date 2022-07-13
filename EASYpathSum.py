# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        #create another function inside to input current sum val 
        #why not just use a variable?
        
        def depthFirstSearch(node, curSum):
            #if node has no values, it can't reach the target
            if not node: return False
            #add current node value to curSum
            curSum += node.val
            #this checks if it's a leaf node-- if it doesn't have left or right it must be the end
            if not node.left and not node.right:
                return curSum == targetSum
            
            #if it hasn't been stopped yet, run it recursively 
            #first on left, then on right
            #if either of these are true it'll spit True out
            return (depthFirstSearch(node.left, curSum) or depthFirstSearch(node.right, curSum))
        #call the function
        # put the root itself in, and start curSum at 0
        return depthFirstSearch(root, 0)