# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # if nithing, return nothing
        if head is None:
            return None
        # dummy style -- learn
        
        current = dummy = ListNode(0)
        while head is not None:
            if head.val == val:
                head = head.next
                continue
            else:
                current.next = ListNode(head.val)
            
            current = current.next
            head = head.next
        
        return dummy.next