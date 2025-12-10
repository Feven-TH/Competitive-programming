# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        length,curr = 0, head
        while curr:
            length += 1
            curr = curr.next
        
        p = length -1
        res = 0
        while head:
            if head.val:
                res += 2**p
            head = head.next
            p -= 1
        return res
