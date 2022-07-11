# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # if root is null the tree has no depth
        if not root: return 0
        #depth counter
        depth = 0
        #classic empty answer list
        ansList = []
        #add current root to ansList
        ansList.append(root)
        
        #while ansList not empty
        while ansList:
            depth +=1
            #new temp ans list
            temp =  []
            
            for i in ansList:
                if i.left:
                    temp.append(i.left)
                if i.right:
                    temp.append(i.right)
            
            ansList = temp
            
        return depth
            
            