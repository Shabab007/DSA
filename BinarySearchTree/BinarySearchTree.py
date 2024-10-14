import sys

sys.path.append("/Users/shabab/Chores/Projects/python/DSA")
import QueueLinkedList.create as queue

class BSTNode:
    def __init__(self,data):
        self.data = data
        self.leftChild= None
        self.rightChild= None
    
def insertNode(rootNode,nodeValue):
    if rootNode.data == None:
        rootNode.data = nodeValue
    elif nodeValue >= rootNode.data:
        if rootNode.rightChild is None:
            rootNode.rightChild = BSTNode(nodeValue)
        else:
            insertNode(rootNode.rightChild,nodeValue)
    elif nodeValue <= rootNode.data:
        if rootNode.leftChild is None:
            rootNode.leftChild = BSTNode(nodeValue)
        else:
            insertNode(rootNode.leftChild,nodeValue)
    return "The node has been inserted successfully"

def searchNode(rootNode,nodeValue):
    if rootNode.data == nodeValue:
        print("Node found at root")
    elif nodeValue >= rootNode.data:
        if rootNode.rightChild.data == nodeValue:
            print(f"Node found at right of {rootNode.data}")
        else:
            searchNode(rootNode.rightChild,nodeValue)
    elif nodeValue <= rootNode.data:
        if rootNode.leftChild.data == nodeValue:
            print(f"Node found at left of {rootNode.data}")
        else:
            searchNode(rootNode.leftChild,nodeValue)
    else:
        print("Node not found in BST")

def minValueNode(bstNode):
    current = bstNode
    while(current.leftChild is not None):
        current = current.leftChild
    return current

def levelOrderTraversal(rootNode):
  if not rootNode:
    return
  else:
    customQueue = queue.Queue()
    customQueue.enqueue(rootNode)
    while not(customQueue.is_empty()):
      root = customQueue.dequeue()
      print(root.data)
      # print(root.value.data)
      if(root.leftChild is not None):
        customQueue.enqueue(root.leftChild)
      if(root.rightChild is not None):
        customQueue.enqueue(root.rightChild)

def deleteNode(rootNode,nodeValue):
    if rootNode is None:
        return rootNode
    if nodeValue < rootNode.data:
        rootNode.leftChild = deleteNode(rootNode.leftChild,nodeValue)
    elif nodeValue > rootNode.data:
        rootNode.rightChild = deleteNode(rootNode.rightChild,nodeValue)
    else:
        if rootNode.leftChild is None:
            temp =  rootNode.rightCild
            rootNode = None
            return temp
        if rootNode.rightChild is None:
            temp =  rootNode.leftChild
            rootNode = None
            return temp
        temp = minValueNode(rootNode.rightChild)
        rootNode.data = temp
        rootNode.rightChild = deleteNode(rootNode.rightChild, temp.data)
    return rootNode

def deleteBST(rootNode):
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None


newBST = BSTNode(None)

print(insertNode(newBST,70))
print(insertNode(newBST,50))

print(insertNode(newBST,30))
print(insertNode(newBST,20))

print(insertNode(newBST,100))
print(insertNode(newBST,40))

print(insertNode(newBST,80))
print(insertNode(newBST,50))

print(insertNode(newBST,55))
print(insertNode(newBST,10))

# searchNode(newBST,20)

levelOrderTraversal(newBST)
deleteNode(newBST,100)

print("------------------------------>>>>>>")

levelOrderTraversal(newBST)
# print(newBST.data)
# print(newBST.leftChild.data)
        