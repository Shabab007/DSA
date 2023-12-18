from random import randint
class Node:
  def __init__(self,value=None) -> None:
    self.value=value
    self.next= None
    self.prev = None

class LinkedList:
   def __init__ (self):
    self.head= None
    self.tail= None
   def __iter__(self):
     node=self.head
     while node:
       yield node
       node =node.next
   def __str__(self) -> str:
     values = [str(node.value) for node in self]
     return " -> ".join(values)
   def __len__(self):
     count =0 
     node=self.head
     while node:
       count+=1
       node =node.next
     return count
   def add(self,value):
     if self.head is None:
       node = Node(value)
       self.head = node
       self.tail = node
     else: 
       self.tail.next= Node(value)
       self.tail = self.tail.next  
     return self.tail
   def generate(self,n,min_value,max_value):
     self.head = None
     self.head = None
     for i in range(n):
       self.add(randint(min_value,max_value))
     return self
   
customLL = LinkedList()
customLL.generate(10,0,99)
print(customLL)
print(len(customLL))