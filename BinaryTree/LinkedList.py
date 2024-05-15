import sys

sys.path.append("/Users/shabab/Chores/Projects/python/DSA")

import QueueLinkedList.create as queue
class TreeNode:
  def __init__(self, data):
    self.data = data
    self.leftChild = None
    self.rightChild = None

newBT = TreeNode("Drinks")
leftChild= TreeNode("Hot")
rightChild= TreeNode("Cold")
tea= TreeNode("tea")
coffee= TreeNode("coffee")
leftChild.leftChild=tea
leftChild.rightChild=coffee
newBT.leftChild=leftChild
newBT.rightChild=rightChild


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
  if not rootNode:
    return "The node not exist in BT"
  customQueue = queue.Queue()
  customQueue.enqueue(rootNode)
  while not(customQueue.is_empty()):
    root = customQueue.dequeue()
    if(root.data == nodeValue):
      return root.data
    # print(root.value.data)
    if(root.leftChild is not None):
      customQueue.enqueue(root.leftChild)
    if(root.rightChild is not None):
      customQueue.enqueue(root.rightChild)
  return "Not found"

def insertNode(rootNode,newNode):
  if not rootNode:
    rootNode = newNode
    return "Successfully inserted in root"
  customQueue = queue.Queue()
  customQueue.enqueue(rootNode)
  while not(customQueue.is_empty()):
    root = customQueue.dequeue()
    if(root.leftChild is not None):
      customQueue.enqueue(root.leftChild)
    else:
      root.leftChild= newNode
      return "Successfully added in left node of" + root.data
    if(root.rightChild is not None):
      customQueue.enqueue(root.rightChild)
    else:
      root.rightChild= newNode
      return "Successfully added in right node of" + root.data

def getDeepestNode(rootNode):
  if not rootNode:
    return
  customQueue = queue.Queue()
  customQueue.enqueue(rootNode)
  while not(customQueue.is_empty()):
    root = customQueue.dequeue()
    if(root.leftChild is not None):
      customQueue.enqueue(root.leftChild)
    if(root.rightChild is not None):
      customQueue.enqueue(root.rightChild)
  deepestNode = root
  return deepestNode

def deleteDeepestNode(rootNode,node):
  if not rootNode:
    return
  customQueue = queue.Queue()
  customQueue.enqueue(rootNode)
  while not(customQueue.is_empty()):
    root = customQueue.dequeue()
    if root is node:
      root =None
      return
    if(root.leftChild):
      if root.leftChild is node:
        root.leftChild = None
        return
      else:
        customQueue.enqueue(root.leftChild)
    if(root.rightChild):
      if root.rightChild is node:
        root.rightChild = None
        return
      else:
        customQueue.enqueue(root.rightChild)

def deleteNodeBT(rootNode,node):
  if not rootNode:
    return "node does not exist"
  customQueue = queue.Queue()
  customQueue.enqueue(rootNode)
  while not(customQueue.is_empty()):
    root = customQueue.dequeue()
    if root.data == node:
      dNode= getDeepestNode(rootNode)
      root.data =dNode.data
      deleteDeepestNode(rootNode, dNode)
      return "the node deleted"
    if(root.leftChild is not None):
      customQueue.enqueue(root.leftChild)
    if(root.rightChild is not None):
      customQueue.enqueue(root.rightChild)
  return "Failed to delete"

def deleteBT(rootNode):
  rootNode.data = None
  rootNode.leftChild = None
  rootNode.rightChild = None
  return "The BT has been deleted successfully"
# preOrderTraversal(newBT)

# print("InOrderTravarsal")
# inOrderTraversal(newBT)

# print("PostOrderTravarsal")
# postOrderTraversal(newBT)

# print("levelOrderTravarsal")
# levelOrderTraversal(newBT)

# print("search")
# print(searchNode(newBT,"Cold"))

newNode = TreeNode("Cola")
print("insert")
# print(insertNode(newBT,newNode))
# # levelOrderTraversal(newBT)

# levelOrderTraversal(newBT)
# deepestNode=getDeepestNode(newBT)
# deleteDeepestNode(newBT,deepestNode)
# levelOrderTraversal(newBT)

deleteNodeBT(newBT,"tea")
levelOrderTraversal(newBT)
