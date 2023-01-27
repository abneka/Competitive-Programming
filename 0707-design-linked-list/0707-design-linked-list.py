class ListNode():
    
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        

    def get(self, index: int) -> int:
        if index < 0 or index >= self.length:
            return -1
        
        cur = self.head
        
        while index != 0:
            
            cur = cur.next
            index -= 1
            
        return cur.val
            

    def addAtHead(self, val: int) -> None:
        new_node = ListNode( val )
        
        new_node.next = self.head
        
        if self.head:
            self.head.prev = new_node
        
        self.head = new_node
               
        self.length += 1
        
        if self.length == 1:
            self.tail = new_node

    def addAtTail(self, val: int) -> None:
        new_node = ListNode( val )
        
        new_node.prev = self.tail
        
        if self.tail:
            self.tail.next = new_node
        
        self.tail = new_node
        
        self.length += 1
        
        if self.length == 1:
            self.head = new_node

        
    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.length:
            return
        
        elif index == 0:
            self.addAtHead( val )
        
        elif index == self.length:
            self.addAtTail( val )
            
        else:
                
            cur = self.head
            while index-1 != 0:

                cur = cur.next
                index -= 1

            new_node = ListNode( val )

            new_node.next = cur.next
            cur.next.prev = new_node

            cur.next = new_node
            new_node.prev = cur
            
            self.length += 1


    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.length:
            return
        
        elif index == 0:
            
            if self.head.next:
                self.head.next.prev = None
                
            self.head = self.head.next
            
            self.length -= 1
            
            if self.length == 0:
                self.tail = None
        
        elif index == self.length-1:
            
            if self.tail.prev:
                self.tail.prev.next = None
            
            self.tail = self.tail.prev
            
            self.length -= 1
            
            if self.length == 0:
                self.head = None
            
        else:
                
            cur = self.head
            while index-1 != 0:

                cur = cur.next
                index -= 1

            cur.next = cur.next.next
            cur.next.prev = cur
            
            self.length -= 1
                
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)