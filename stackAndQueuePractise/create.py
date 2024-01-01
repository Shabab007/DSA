from LinkedListStack.LinkedListStack import Node

class Stack:
    def __init__(self):
        self.top= None
        self.minNode = None
    def min(self):
        if not self.minNode:
            return None
        else:
            return self.minNode.value
    def push(self,item):
        if self.minNode and (self.minNode.value <item):
            self.minNode=Node(value=self.minNode.value, next=self.minNode)
        else:
            self.minNode =Node(value=item, next=self.minNode)
        self.top = Node(value=item, next=self.top)
    def pop(self):
        if not self.top:
            return None
        if self.top == self.minNode:
            self.minNode=self.minNode.next
        value =self.top.value
        self.top = self.top.next
        return value
    
customStack =Stack()
customStack.push(5)
print(customStack.min())
customStack.push(4)
print(customStack.min())
customStack.push(3)
print(customStack.min())
customStack.pop()
print(customStack.min())
