# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ansList = []
        def inorder(root):
            #if root is null
            if not root:
                #just spit it out
                return []
            #run function on the left
            inorder(root.left)
            #add the value to the answer lit
            ansList.append(root.val)
            #run it on the right
            inorder(root.right)
        #call the function
        inorder(root)
        #bring the answer list home
        return ansList
        