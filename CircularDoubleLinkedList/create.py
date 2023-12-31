class Node:
    def __init__(self,value):
        self.value = value
        self.prev = None
        self.next = None

class CircularDoublyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
    def CDLL(self,value):
        newNode = Node(value)
        self.head = newNode
        self.tail = newNode
        newNode.next = newNode
        newNode.prev = newNode
        return "Cicular Doubly Linked List is created"
    def __iter__(self):
        if self.head is None:
            return "No list found"
        else:
            tempNode = self.head
            while tempNode:
                yield tempNode
                tempNode=tempNode.next
                if tempNode == self.tail.next:
                    break
    def ReverseTravarseList(self):
     if self.head is None:
       return "There is no list"
     else:
         tempNode = self.tail
         while tempNode:
             print (tempNode.value)
             tempNode = tempNode.prev
             if tempNode is self.head.prev:
                 break

    def travarseList(self):
        tempNode = self.head
        while tempNode:
            print(tempNode.value) 
            tempNode = tempNode.next
            if tempNode is self.tail.next:
                break
    def removeNode(self,location):
        if self.head is None:
            return "No list found"
        elif (location == -1 or location ==0) and self.head == self.tail:
            print("skjdks")
            self.head.next=None
            self.head.prev = None        
            self.head = None
            self.tail=None
        elif location == 0:
            self.head =self.head.next 
            self.head.prev = self.tail
            self.tail.next = self.head
        elif location == -1:

            self.tail =self.tail.prev
            self.tail.next = self.head
            self.head.prev =self.tail
        else:
            tempNode = self.head
            index = 0
            while index < location-1:
                index+=1
                tempNode=tempNode.next
                if tempNode is self.tail.next:
                    return "location is incorrect"
            tempNode.next =tempNode.next.next
            tempNode.next.prev = tempNode
        
    def searchNode(self,value):
        if self.head is None:
            return "No list found"
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value ==value:
                    return tempNode.value
                tempNode= tempNode.next
                if tempNode is self.tail.next:
                    break
            return "No value found"
    def deleteWholeList(self):
        if self.head is None:
            return "No list found"
        else:
            self.tail.next = None
            tempNode = self.head
            while tempNode:
             tempNode.prev = None
             tempNode = tempNode.next
            self.head = None
            self.tail = None
    def insertNode(self,value,location):
        if self.head is None:
            return "No list found"
        else:
            newNode=Node(value)
            if location ==0 : 
               newNode.next = self.head
               newNode.prev = self.tail
               self.head.prev = newNode
               self.head = newNode
               self.tail.next = newNode
            elif location == -1:
               newNode.prev = self.tail
               newNode.next = self.tail.next
               self.head.prev = newNode
               self.tail.next = newNode
               self.tail = newNode
            else:
                tempNode = self.head
                count = 0 
                while count < location-1:
                 tempNode= tempNode.next
                 count +=1
                newNode.next = tempNode.next
                newNode.prev =tempNode
                newNode.next.prev=newNode
                tempNode.next = newNode
            return "successfully inserted"    
            

circularDll = CircularDoublyLinkedList()
circularDll.CDLL(5)
print([node.value for node in circularDll])
circularDll.insertNode(0,0)
circularDll.insertNode(1,-1)
circularDll.insertNode(2,2)

# circularDll.travarseList()
# circularDll.ReverseTravarseList()
print([node.value for node in circularDll])
# print(circularDll.searchNode(5))

circularDll.deleteWholeList()
print([node.value for node in circularDll])