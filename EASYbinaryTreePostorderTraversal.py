# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #if root is null return empty list
        if root == None: return []
        #look left, look right, add value
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]