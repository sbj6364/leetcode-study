# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        values = []
        curr = head
        while curr:
            values.append(curr.val)
            curr = curr.next

        max_sum = 0
        n = len(values)
        for i in range(n // 2):
            twin_sum = values[i] + values[n - 1 - i]
            max_sum = max(max_sum, twin_sum)

        return max_sum