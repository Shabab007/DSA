class Queue:
    def __init__(self,maxSize) -> None:
        self.list=[None]*maxSize
        self.maxSize = maxSize
        self.start =-1
        self.top=-1
    def __str__(self):
        values = [str(x) for x in self.list]
        return " ".join(values)  
    def is_full(self):
       if self.top +1 == self.start:
          return True
       elif self.start ==0 and self.top+1==self.maxSize:
          return True
       else:
          return False
       
    def is_empty(self):
        if self.top == -1:
            return True
        else:
            return False
    def enqueue(self,value):
      if self.is_full():
        return "List is empty"
      else:
        if self.top+1 == self.maxSize:
           self.top=0
        else:
           self.top+=1
           if self.start ==-1:
              self.start=0
        self.list[self.top]=value
        return f"Queue value inserted at {self.top} index"
    def dequeue(self):
      if self.is_empty():
        return "List is empty"
      else:
        firstElement = self.list[self.start]
        start = self.start
        if self.start == self.top:
           self.start =-1
           self.top =-1
        elif self.start+1==self.maxSize:
           self.start=0
        else:
           self.start+=1
        self.list[start]=None
        return firstElement
    def peek(self):
      if self.is_empty():
        return "List is empty"
      else:
        return self.list[self.start]
    def delete(self):
        self.list=self.maxSize*[None]
        self.top =-1
        self.start=-1

customQueue = Queue(3)
customQueue.enqueue(4)
customQueue.enqueue(5)
customQueue.enqueue(6)
# print(customQueue)
# customQueue.dequeue()
# print(customQueue.peek())
print(customQueue)
print(customQueue.dequeue())
print(customQueue.peek())
print(customQueue)
# customQueue.delete()
# print(customQueue.is_empty())
# print(customQueue.is_full())

