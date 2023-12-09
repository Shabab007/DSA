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

   def travarseList(self):
     if self.head is None:
       print("Linked list does not exist")
     node =self.head
     while node:
       print(node.value)
       node = node.next  

   def searchValue(self,value):
     if self.head is None:
       print("Linked list does not exist")
     node =self.head
     while node:
       if node.value == value:
         return node.value
       node = node.next  
     return "The value does not exist in linked list"
   

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
       while index < location -1:
         tempNode = tempNode.next
         index +=1
       nextNode = tempNode.next
       tempNode.next=newNode
       newNode.next=nextNode
       if tempNode == self.tail:
         self.tail= newNode  
   
   def deleteNodeFromList(self,location):
     if self.head is None:
        print("The sll does not exist")
     if location ==0:
       if self.head== self.tail:
         self.head = None
         self.tail = None
       else:
         self.head = self.head.next
     elif location ==-1:
       if self.head== self.tail:
         self.head = None
         self.tail = None
       else:
         node= self.head
         while node is not None:
           if node.next == self.tail:
            break
           node=node.next
         node.next=None  
         self.tail=node  
     else:
       tempNode=self.head
       index=0
       while index < location-1:
         tempNode = tempNode.next
         index +=1
       nextNode = tempNode.next
       print(tempNode.value)  
       tempNode.next = nextNode.next




singlyLinkedList = SLinkedList()
singlyLinkedList.inserSLL(2,1)
singlyLinkedList.inserSLL(3,2)
singlyLinkedList.inserSLL(4,3)
singlyLinkedList.inserSLL(5,4)
singlyLinkedList.inserSLL(1,0)
singlyLinkedList.inserSLL(7,2)
print([node.value for node in singlyLinkedList])
singlyLinkedList.deleteNodeFromList(9)
print([node.value for node in singlyLinkedList])
