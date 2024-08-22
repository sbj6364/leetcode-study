# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
        
        middle_index = length // 2
        
        current = head
        for _ in range(middle_index - 1):
            current = current.next
        
        if current.next:
            current.next = current.next.next
        
        return head