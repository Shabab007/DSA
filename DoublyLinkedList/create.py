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
   def travarseList(self):
     if self.head is None:
       return "There is no list"
     node = self.head
     while node:
       print(node.value)
       node= node.next
   def ReverseTravarseList(self):
     if self.head is None:
       return "There is no list"
     node = self.tail
     while node:
       print(node.value)
       node= node.prev

   def searchValue(self,value):
     if self.head is None:
       return "There is no list"
     node = self.head
     while node:
       if node.value == value:
        return node.value
       node= node.next
   def removeNode(self,location) :
     if self.head is None:
       return "No list found"
     else:
       if self.head ==self.tail and (location ==0 or location ==-1):
        print(location)
        self.head=None   
        self.tail= None
       elif location == 0:
        self.head = self.head.next
        self.head.prev = None
       elif location == -1:
        self.tail = self.tail.prev
        self.tail.next = None
       else:
         tempNode=self.head
         index= 0
         while index < location-1:
           index +=1
           tempNode = tempNode.next
         tempNode.next = tempNode.next.next
         tempNode.next.prev = tempNode 
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
     print("The Node has not been found on list")
     
   


doublyLL= DoublyLinkedList()
doublyLL.createLinkedList(5)

print ([node.value for node in doublyLL])

doublyLL.insertNode(0,0)
doublyLL.insertNode(2,-1)
doublyLL.insertNode(6,2)

print ([node.value for node in doublyLL])

doublyLL.removeNode(2)


print ([node.value for node in doublyLL])