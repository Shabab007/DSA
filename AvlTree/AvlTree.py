import sys

sys.path.append("/Users/shabab/Chores/Projects/python/DSA")
import QueueLinkedList.create as queue

class AVLTree:

    def __init__(self,data):
        self.data=data
        self.leftChild= None
        self.rightChild = None
        self.height= 1

def preOrderTraversal(rootNode):
  if not rootNode:
    return
  print(rootNode.data)
  preOrderTraversal(rootNode.leftChild)
  preOrderTraversal(rootNode.rightChild)
def inOrderTraversal(rootNode):
  if not rootNode:
    return
  inOrderTraversal(rootNode.leftChild)
  print(rootNode.data)
  inOrderTraversal(rootNode.rightChild)
def postOrderTraversal(rootNode):
  if not rootNode:
    return
  postOrderTraversal(rootNode.leftChild)
  postOrderTraversal(rootNode.rightChild)
  print(rootNode.data)

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

def searchNode(rootNode,nodeValue):
    if rootNode.data == nodeValue:
        print("Node found at root")
    elif nodeValue > rootNode.data:
        if rootNode.rightChild.data == nodeValue:
            print(f"Node found at right of {rootNode.data}")
        else:
            searchNode(rootNode.rightChild,nodeValue)
    elif nodeValue < rootNode.data:
        if rootNode.leftChild.data == nodeValue:
            print(f"Node found at left of {rootNode.data}")
        else:
            searchNode(rootNode.leftChild,nodeValue)
    else:
        print("Node not found in BST")
def getHeight(rootNode):
   if not rootNode:
      return 0
   return rootNode.height

def rightRotate(disbalanceNode):
   newRoot = disbalanceNode.leftChild
   disbalanceNode.leftChild = disbalanceNode.leftChild.rightChild
   newRoot.rightChild = disbalanceNode
   disbalanceNode.height = 1 + max(getHeight(disbalanceNode.leftChild),getHeight(disbalanceNode.rightChild))    
   newRoot.height = 1 + max(getHeight(newRoot.leftChild),getHeight(newRoot.rightChild))  
   return newRoot

def leftRotate(disbalanceNode):
   newRoot = disbalanceNode.rightChild
   disbalanceNode.rightChild = disbalanceNode.rightChild.leftChild
   newRoot.leftChild = disbalanceNode
   disbalanceNode.height = 1 + max(getHeight(disbalanceNode.leftChild),getHeight(disbalanceNode.rightChild))    
   newRoot.height = 1 + max(getHeight(newRoot.leftChild),getHeight(newRoot.rightChild))  
   return newRoot

def getBalance(rootNode):
   if not rootNode:
      return 0
   return getHeight(rootNode.leftChild) - getHeight(rootNode.rightChild)


def insertNode(rootNode, nodeValue):
   if not rootNode:
      return AVLTree(nodeValue)
   elif nodeValue < rootNode.data:
      rootNode.leftChild = insertNode(rootNode.leftChild,nodeValue)
   else:
      rootNode.rightChild = insertNode(rootNode.rightChild,nodeValue)
  
   rootNode.height = 1 + max(getHeight(rootNode.leftChild),getHeight(rootNode.rightChild))
   balance = getBalance(rootNode)
   if balance > 1  and nodeValue < rootNode.leftChild.data:
      return rightRotate(rootNode)
   if balance > 1  and nodeValue > rootNode.leftChild.data:
      rootNode.leftChild = leftRotate(rootNode.leftChild)
      return rightRotate(rootNode)
   if balance < -1  and nodeValue > rootNode.rightChild.data:
      return leftRotate(rootNode)
   if balance > 1  and nodeValue < rootNode.rightChild.data: 
      rootNode.rightChild = rightRotate(rootNode.rightChild)
      return leftRotate(rootNode)
   return rootNode
   
newAvl = AVLTree(5)
newAvl = insertNode(newAvl,10)
newAvl = insertNode(newAvl,15)
newAvl = insertNode(newAvl,20)

levelOrderTraversal(newAvl)
