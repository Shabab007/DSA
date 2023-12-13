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
       pass
   


doublyLL= DoublyLinkedList()
doublyLL.createLinkedList(5)

print ([node.value for node in doublyLL])