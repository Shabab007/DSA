class Node:
  def __init__(self,value=None) -> None:
    self.value=value
    self.next= None

class SLinkedList:
   def __init__ (self):
    self.head= None
    self.tail= None
   def __iter__(self):
     node=self.head
     while node:
       yield node
       node =node.next

   def inserSLL(self,value,location):
     newNode= Node(value)
     if self.head is None:
       self.head=newNode
       self.tail= newNode
     elif location == 0:
       newNode.next= self.head
       self.head = newNode
     elif location == -1:
       newNode.next= None
       self.tail.next = newNode
       self.tail = newNode
     else:
       tempNode = self.head
       index =0 
       while index < location -1 and tempNode.next is not None:
         tempNode = tempNode.next
         index +=1
       nextNode = tempNode.next
       tempNode.next=newNode
       newNode.next=nextNode
       if tempNode == self.tail:
         self.tail= newNode  

singlyLinkedList = SLinkedList()
singlyLinkedList.inserSLL(2,1)

singlyLinkedList.inserSLL(3,2)
singlyLinkedList.inserSLL(4,3)
singlyLinkedList.inserSLL(5,4)
singlyLinkedList.inserSLL(1,0)
singlyLinkedList.inserSLL(7,2)

print([node.value for node in singlyLinkedList])