class Node:
  def __init__(self,value=None) -> None:
    self.value=value
    self.next= None
    self.prev= None

class DoublyLinkedList:
   def __init__ (self):
    self.head= None
    self.tail= None
   def __iter__(self):
     node= self.head
     while node:
       yield node
       node= node.next

   def createLinkedList(self,value):
     node=Node(value)
     self.head = node
     self.tail = node
     return "The Dll is created Successfully"
   def insertNode(self,value,location):
     if self.head is None:
       return "No list found"
     else:
       node=Node(value)
       if location == 0: 
         node.next =self.head
         self.head.prev = node
         self.head =node
       elif location == -1:
         node.prev =self.tail
         self.tail.next = node
         self.tail =node
       else:
         count = 0
         tempNode = self.head
         while count < location -1:
           tempNode=tempNode.next
           count +=1
         node.next = tempNode.next
         node.prev = tempNode
         tempNode.next.prev = node
         tempNode.next = node
   


doublyLL= DoublyLinkedList()
doublyLL.createLinkedList(5)

print ([node.value for node in doublyLL])

doublyLL.insertNode(0,0)
doublyLL.insertNode(2,-1)
doublyLL.insertNode(6,2)

print ([node.value for node in doublyLL])