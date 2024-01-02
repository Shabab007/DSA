class Node:
    def __init__(self,value,next=None) -> None:
        self.value=value
        self.next=next

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail= None
    def __iter__(self):
        currNode= self.head
        while currNode:
            yield currNode
            currNode = currNode.next
class Queue:
    def __init__(self):
     self.linkedList = LinkedList()
    def __str__(self) -> str:
     values=[str(x.value) for x in self.linkedList]
     return " ".join(values)
    def is_empty(self):
       if self.linkedList.head is None:
          return True
       else:
          return False
    def enqueue(self,value):
       newNode = Node(value)
       if self.linkedList.head is None:
          self.linkedList.head = newNode
          self.linkedList.tail = newNode
       else:
          self.linkedList.tail.next = newNode
          self.linkedList.tail = newNode
    def dequeue(self):
       if self.is_empty():
          return "Queue is empty"
       else:
        value = self.linkedList.head.value
        if self.linkedList.head == self.linkedList.tail:
             self.linkedList.head=None
             self.linkedList.tail=None
        else:      
          self.linkedList.head = self.linkedList.head.next
        return value
    def peek(self):
       if self.is_empty():
          return "Queue is empty"
       else:
          value = self.linkedList.head.value
          return value
    def delete(self):
       self.linkedList.head=None
       self.linkedList.tail=None

customQueue = Queue()
customQueue.enqueue(4)
customQueue.enqueue(5)
customQueue.enqueue(6)
# print(customQueue)
customQueue.dequeue()
# print(customQueue.peek())
print(customQueue)