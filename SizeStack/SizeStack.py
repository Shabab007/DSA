class Stack:
    def __init__(self,maxSize) -> None:
        self.list=[]
        self.maxSize = maxSize
    def __str__(self):
        values = self.list.reverse()
        # print(values)
        # print(self.list)
        values=[str(value) for value in self.list]
        return '\n'.join(values)
    def is_empty(self):
        if self.list ==[]:
            return True
        else:
            return False
    def is_full(self):
        if len(self.list)==self.maxSize:
            return True
        else:
            return False    
    def push(self,value):
        if self.is_full():
            return "Stack is full"
        self.list.append(value)
        return "The element has been inserted successfully"
    def pop(self):
        if self.list ==[]:
            return "There is no element here"
        else:   
            return self.list.pop()
    def peek(self):
        if self.list ==[]:
            return "There is no element here"
        else:   
            return self.list[len(self.list)-1]
    def delete(self):
        self.list= None



customStack = Stack(4)
customStack.push(1)
customStack.push(2)
customStack.push(3)
customStack.push(4)
customStack.push(4)
customStack.push(4)
# customStack.pop()
# print(customStack.peek())
print(customStack)  
# print(customStack.is_empty())