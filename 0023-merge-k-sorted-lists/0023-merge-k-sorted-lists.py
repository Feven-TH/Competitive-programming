# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        arr = [[] for i in range(len(lists))]
        for i in range(len(lists)):
            curr = lists[i]
            while curr:
                arr[i].append(curr.val)
                curr = curr.next
        
        heap = []
        for i in range(len(arr)):
            if arr[i]:
                heapq.heappush(heap, (arr[i][0] ,i ,0))
        
        dummy = ListNode(0)
        head = dummy
        while heap:
            val, i ,j =  heappop(heap)
            dummy.next = ListNode(val)
            dummy = dummy.next
            if j + 1 < len(arr[i]):
                heappush(heap ,(arr[i][j +1] , i, j+ 1)) 
       
        return head.next
            

        
         
