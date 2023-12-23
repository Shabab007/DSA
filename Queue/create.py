class Queue:
    def __init__(self) -> None:
        self.list=[]
    def __str__(self):
        values = [str(x) for x in self.list]
        return " ".join(values)  
    def is_empty(self):
        if self.list == []:
            return True
        else:
            return False
    def enqueue(self,value):
        self.list.append(value)
        return "The element inserted successfully"
    def dequeue(self):
      if self.is_empty():
        return "List is empty"
      else:
        self.list.pop(0)
    def peek(self):
      if self.is_empty():
        return "List is empty"
      else:
        return self.list[0]
    def delete(self):
        self.list=[]

customQueue = Queue()
customQueue.enqueue(4)
customQueue.enqueue(5)
customQueue.enqueue(6)
print(customQueue)
customQueue.dequeue()
print(customQueue.peek())
print(customQueue)
customQueue.delete()
print(customQueue)