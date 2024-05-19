class BinaryTree:
    def __init__(self,size):
        self.customList = size * [None]
        self.lastUsedIndex = 0
        self.maxSize = size
    def insertNode(self,value):
        if self.lastUsedIndex == self.maxSize:
            return "Binary tree is full"
        self.customList[self.lastUsedIndex+1]= value
        self.lastUsedIndex+=1
        return f"The {value} has been successfully inserted into {self.lastUsedIndex}"
    def searchNode(self,nodeValue):
        for i in range(len(self.customList)):
            if self.customList[i]== nodeValue:
                return f"Node found in index {i}"
        return "Not found"
    def preOrderTraversal(self,index):
        if index > self.lastUsedIndex:
            return 
        print(self.customList[index])
        self.preOrderTraversal(index*2)
        self.preOrderTraversal(index*2+1)
    def inOrderTraversal(self,index):
        if index > self.lastUsedIndex:
            return 
        self.inOrderTraversal(index*2)
        print(self.customList[index])
        self.inOrderTraversal(index*2+1)
    def postOrderTraversal(self,index):
        if index > self.lastUsedIndex:
            return 
        self.postOrderTraversal(index*2)
        self.postOrderTraversal(index*2+1)
        print(self.customList[index])
    def levelOrderTraversal(self,index):
       for i in range(index, self.lastUsedIndex+1):
            print(self.customList[i])
    def deleteNode(self,value):
        if self.lastUsedIndex == 0:
            return "There is no node to delete"
        for i in range(1, self.lastUsedIndex+1):
            if self.customList[i] == value:
                self.customList[i]= self.customList[self.lastUsedIndex]
                self.customList[i]= None
                self.lastUsedIndex -=1
                return "The node has been deleted successfully"
    def deleteBT(self):
        self.customList=None

newBT = BinaryTree(8)
newBT.insertNode("Drinks")
newBT.insertNode("Hot")
newBT.insertNode("Cold")
newBT.insertNode("Tea")
newBT.insertNode("Coffee")


newBT.deleteNode("Tea")
newBT.levelOrderTraversal(1)