class MyLinkedList:

    def __init__(self, val = 0, next=None):
        self.next = next
        self.val = val

    head = None
    def get(self, index: int) -> int:
        i = 0
        curr = self.head
        while curr and i < index:
            curr = curr.next
            i += 1
        if curr and i == index:
            return curr.val
        return -1

    def addAtHead(self, val: int) -> None:
        node = MyLinkedList(val)
        node.next = self.head
        self.head = node
        
    def addAtTail(self, val: int) -> None:
        node = MyLinkedList(val)
        if not self.head:          
            self.head = node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = node

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
            return
        i = 0
        node = MyLinkedList(val)
        curr = self.head
        while curr and i < index-1:
            curr = curr.next
            i += 1

        if not curr:
            return
            
        nxt = curr.next 
        curr.next = node
        node.next = nxt
            
    def deleteAtIndex(self, index: int) -> None:
        if not self.head:
            return
        if index == 0:
            self.head = self.head.next
            return

        i = 0
        curr = self.head
        while curr and i < index-1:
            curr = curr.next
            i += 1
    
        if not curr or not curr.next:
            return
        
        curr.next = curr.next.next



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)