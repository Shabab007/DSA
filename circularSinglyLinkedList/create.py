class Node:
  def __init__(self,value=None) -> None:
    self.value=value
    self.next= None

class circularSLinkedList:
   def __init__ (self):
    self.head= None
    self.tail= None
   def __iter__(self):
     node=self.head
     while node:
       yield node
       if node.next == self.head:
          break
       node =node.next
   def csll(self,nodeValue):
     newNode=Node(nodeValue)
     newNode.next=newNode
     self.head=newNode
     self.tail=newNode
     return "circular singly linked list created"
   
cirularSll=  circularSLinkedList()  
cirularSll.csll(1)

print([node.value for node in cirularSll])