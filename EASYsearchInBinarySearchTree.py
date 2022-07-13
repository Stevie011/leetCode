# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        #standard syntax to bring root val in
        current = root
        #stops when current no longer has val
        while current:
            #if current val equals the target val
            if current.val == val:
                return current
            #if val greater than root node, go right, else go left
            elif current.val > val:
                current = current.left
            else:
                current = current.right
        #bring it home
        return current
        