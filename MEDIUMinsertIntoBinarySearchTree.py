# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        #classic empty tree edge case
        if not root: return TreeNode(val)
        
        def insert(node, val):
            #bst sorted left and right -- need to find place to insert val
            #so if val greater, go right
            if val > node.val:
                #check if there's an empty space there
                if not node.right:
                    #if space, insert the value there
                    node.right = TreeNode(val)
                else:
                    #else, keep traversing recursively
                    insert(node.right, val)
            #if val is less than current node's val, go left
            else:
                #check for space
                if not node.left:
                    #if space, insert the value there
                    node.left = TreeNode(val)
                else:
                    #else, keep traversing recursively
                    insert(node.left, val)
        #call the function, putting vals specced in question in there       
        insert(root, val)
        #bring it home
        return root
    
        