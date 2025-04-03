# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def merge(left, right):
            curr = ListNode(0)
            res = curr

            while left and right:
                if left.val <= right.val:
                    curr.next = left
                    left = left.next
                else:
                    curr.next = right
                    right = right.next
                curr = curr.next

            if left:
                curr.next = left
            if right:
                curr.next = right

            return res.next

        def split(head):
            if not head or not head.next:
                return head
                
            slow , fast = head , head.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            mid = slow.next
            slow.next = None
            
            left = split(head)
            right = split(mid)

            return merge(left , right)

        return split(head)






