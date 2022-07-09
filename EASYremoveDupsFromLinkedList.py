# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #standard linked list style
        current = head
        #loop ends when current becomes null
        while current:
            #loop ends when current.next becomes null
            #and deletes nodes when they have the same value
            while current.next and current.next.val == current.val:
                current.next = current.next.next
            current = current.next
        return head
        