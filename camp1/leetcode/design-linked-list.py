class Node:
     def __init__(self,value=0):
        self.val=value
        self.next=None
     def __str__(self):
         arr=[self.val]
         temp=self.next

         while temp:
             arr.append(temp.val)
             temp=temp.next
         return "->".join(map(str,arr))
         # to print

class MyLinkedList:

    def __init__(self):
        self.head=Node()  

    def get(self, index: int) -> int:
        temp=self.head

        for _ in range(index+1):
            temp=temp.next
            if temp is None:
                return -1

        return temp.val

    def addAtHead(self, val: int) -> None:
        newNode=Node(val)
        newNode.next=self.head.next
        self.head.next=newNode
        
    def addAtTail(self, val: int) -> None:
       
        temp=self.head
        while temp.next:
            temp=temp.next
        newNode=Node(val)
        temp.next=newNode

    def addAtIndex(self, index: int, val: int) -> None:
        temp=self.head
        for _ in range(index):
            temp=temp.next
            if temp is None:
                return

        newNode=Node(val)
        newNode.next=temp.next
        temp.next=newNode

    def deleteAtIndex(self, index: int) -> None:
        temp=self.head
        for _ in range(index):
            temp=temp.next
            if temp is None:
                return
        if temp.next:
            temp.next=temp.next.next

    
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)