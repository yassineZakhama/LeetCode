from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newHead = ListNode()
        prev = newHead
        
        while head:
            if head.next and head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next
                head = head.next
            
            if not head or not head.next or head.val != head.next.val:
                prev.next = head
                prev = head
                head = head.next if head else None
            
        return newHead.next