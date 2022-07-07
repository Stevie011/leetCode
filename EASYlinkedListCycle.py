# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #slow pointer moves by 1, fast by 2, they go around and when they catch up to each other we find the node
        slowPointer, fastPointer = head, head
        #really need to learn more about this list vibe
        #while loops ends when fastPointer.next doesn't exist anymore
        while fastPointer and fastPointer.next:
            #move slow by 1, fast by 2
            slowPointer = slowPointer.next
            fastPointer = fastPointer.next.next
            if slowPointer == fastPointer:
                return True
        #obvs if true has never been found it must be false
        return False
    

        