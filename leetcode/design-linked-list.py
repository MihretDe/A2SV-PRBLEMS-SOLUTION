class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        temp = self.head 
        if  index >= self.size:
            return -1
        temp = self.head 
        for i in range(0,index):
            temp = temp.next
        
        return temp.val if temp else -1
        # while index:
        #     temp = temp.next
        #     index-=1
        # return temp.val
        

    def addAtHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next=self.head
        self.head=new_node
        self.size+=1

    def addAtTail(self, val: int) -> None:
        new_node = ListNode(val)
        if not self.head:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return 
        new_node = ListNode(val)
        temp = self.head
        if index <= 0:
            new_node.next = self.head
            self.head = new_node
        else:
            for i in range(index-1):
                temp = temp.next
            new_node . next = temp.next
            temp.next= new_node


        
        self.size+=1
    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        temp = self.head
        if index == 0:
            self.head = self.head.next
        else:
            for i in range (index-1):
                temp= temp.next
            temp.next=temp.next.next
        self.size-=1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)