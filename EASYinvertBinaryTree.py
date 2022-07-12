# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
        
            """#swap children
            #classic swap-- bubble sort style
            temp = root.left
            root.left = root.right
            root.right = temp

            #easier way to swap
            root.left, root.right = root.right, root.left

            #recursive bit -- do it again 
            self.invertTree(root.left)
            self.invertTree(root.right)

            """

            #or condense it into one line --= swap and recursion
            
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)

            #bring the root home
            return root
    
    
        