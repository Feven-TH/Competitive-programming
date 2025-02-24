class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        # Initialize pointers for odd and even lists
        odd = head
        even = head.next
        even_head = even  # Keep the head of the even list to reconnect later

        # Traverse and rearrange the nodes
        while even and even.next:
            # Link the next odd node
            odd.next = even.next
            odd = odd.next

            # Link the next even node
            even.next = odd.next
            even = even.next

        # Connect the odd list to the head of the even list
        odd.next = even_head

        return head