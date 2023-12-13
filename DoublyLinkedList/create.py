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
     node.next = None
     node.prev = None
     self.head = node
     self.tail = node
     return "The Dll is created Successfully"
   


doublyLL= DoublyLinkedList()
doublyLL.createLinkedList(5)

print ([node.value for node in doublyLL])