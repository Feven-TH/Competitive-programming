# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow , fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev , curr = None , slow
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        cur = head
        maxx = 0
        while prev and cur:
            maxx = max(cur.val + prev.val , maxx)
            cur = cur.next
            prev = prev.next

        return maxx

        