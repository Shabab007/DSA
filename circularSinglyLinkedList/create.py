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
       node =node.next
       if node == self.tail.next:
          break
   def csll(self,nodeValue):
     newNode=Node(nodeValue)
     newNode.next=newNode
     self.head=newNode
     self.tail=newNode
     return "circular singly linked list created"
   def insertCsll(self,value,location):
      if self.head is None:
        return "head reference is null"
      else:
        newNode=Node(value)
        if location == 0:
          newNode.next= self.head.next
          self.head = newNode
          self.tail.next=newNode
        elif location == -1:
          newNode.next=self.tail.next
          self.tail.next=newNode
          self.tail =newNode
        else:
          tempNode= self.head
          count =0 
          while count < location-1:
            tempNode=tempNode.next
            count +=1
          newNode.next =tempNode.next
          tempNode.next= newNode
        return "The node has been inserted"
   def travarseList(self):
     if self.head is None:
       print("No list found")
     else:
       tempNode=self.head
       while tempNode:
         print(tempNode.value)
         tempNode =tempNode.next
         if tempNode == self.tail.next:
           break
   def findValue(self,value):
     if self.head is None:
       return "No list found"
     else:
       tempNode=self.head
       while tempNode:
         if tempNode.value == value:
          return tempNode.value
         tempNode =tempNode.next
         if tempNode == self.tail.next:
           return "the value does not exist on linked list"    
   def removeAllNode(self):
     self.head = None
     self.tail.next=None
     self.tail = None
   def removeNode(self,location):
     if self.head is None:
       return "No list found"
     else:
       if location ==0 or location ==-1:
        if self.head == self.tail:
            self.head.next=None 
            self.head = None
            self.tail = None  
        elif location == 0:
         self.head = self.head.next
         self.tail.next=self.head
        elif location ==-1:
         print("kdjf")
         tempNode= self.head
         while tempNode:
           tempNode =tempNode.next
           if tempNode.next == self.tail:
            break
         tempNode.next = self.tail.next
         self.tail= tempNode
       else:
         tempNode= self.head
         index=0
         while index < location-1:
           index+=1
           tempNode =tempNode.next
           if tempNode == self.tail.next:
            return "location not found"
         nextNode= tempNode.next
         tempNode.next = nextNode.next
        
           
          
     
   
cirularSll=  circularSLinkedList()  
cirularSll.csll(0)
# cirularSll.insertCsll(0,0)
# cirularSll.insertCsll(2,1)
# cirularSll.insertCsll(3,1)
# cirularSll.insertCsll(4,1)
print([node.value for node in cirularSll])
# cirularSll.travarseList()
# print(cirularSll.findValue(6))

cirularSll.removeNode(-1)
print([node.value for node in cirularSll])