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

print("preOrderTravarsal")
preOrderTraversal(newBT)

print("InOrderTravarsal")
inOrderTraversal(newBT)

print("PostOrderTravarsal")
postOrderTraversal(newBT)

print("levelOrderTravarsal")
levelOrderTraversal(newBT)