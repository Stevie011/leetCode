# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #classic- if root null, return empty list
        if root is None: return []
        queue = [root]
        nextQueue = []
        currLevel = []
        ansList = []
        while queue:
            #go through queue
            for root in queue:
                currLevel.append(root.val)
                #classic setup- execute whichever node/s present
                if root.left:
                    nextQueue.append(root.left)
                if root.right:
                    nextQueue.append(root.right)
            #add current level to ansList
            ansList.append(currLevel)
            #empty out currLevel
            currLevel = []
            queue = nextQueue
            #empty nextQueue again
            nextQueue = []
        return ansList
        
        