class Node:
    def __init__(self,value,next=None) -> None:
        self.value=value
        self.next=next
    def __str__(self) -> str:
        string = str(self.value)
        if self.next:
            string +=",".join(self.next)
        return string

class LinkedList:
    def __init__(self):
        self.head=None
    def __iter__(self):
        currNode= self.head
        while currNode:
            yield currNode
            currNode = currNode.next
            
class Stack:
    def __init__(self) -> None:
        self.linkedList = LinkedList()
    def __str__(self) -> str:
        values=[str(x.value) for x in self.linkedList]
        return "\n".join(values)
    def is_empty(self):
        if self.linkedList.head is None:
            return True
        else:
            return False
    def push(self,value):
        if self.linkedList.head is None:
            self.linkedList.head = Node(value)
        else:
            newNode = Node(value) 
            newNode.next = self.linkedList.head
            self.linkedList.head= newNode
    def pop(self):
        if self.is_empty():
            return "Stack empty"
        else:
           tempNode= self.linkedList.head.value
           self.linkedList.head = self.linkedList.head.next
           return tempNode
    def peek(self):
        if self.is_empty():
            return "Stack empty"
        else:
            return self.linkedList.head.value
    def delete(self):
        self.linkedList.head: None
        

customStack = Stack()
customStack.push(1)
customStack.push(1)
customStack.push(2)
customStack.push(4)
print(customStack)
print("------")
customStack.pop()
print(customStack)