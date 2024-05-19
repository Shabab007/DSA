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
        if rootNode.lefstChild is None:
            rootNode.lefstChild = BSTNode(nodeValue)
        else:
            insertNode(rootNode.lefstChild,nodeValue)
    return "The node has been inserted successfully"
    


newBST = BSTNode(None)

print(insertNode(newBST,70))
print(insertNode(newBST,70))
print(newBST.data)
print(newBST.leftChild.data)
        