class TreeNode:
    def __init__(self,data,children=[]):
        self.data = data
        self.children=children
    def __str__(self, level=0) -> str:
        ret = " " * level + str(self.data) + "\n"
        for child in self.children:
            ret +=child.__str__(level+1)
        return ret
    def addChild(self,TreeNode):
        self.children.append(TreeNode)


root = TreeNode("Drinks",[])
cold_drinks = TreeNode("Cold Drinks",[])
hot_drinks = TreeNode("Hot_Drinks",[])
root.addChild(cold_drinks)
root.addChild(hot_drinks)
tea = TreeNode("Tea",[])
coffe = TreeNode("Coffe",[])
cola = TreeNode("Cola",[])
fanta = TreeNode("Fanta",[])
cold_drinks.addChild(cola)

cold_drinks.addChild(fanta)

hot_drinks.addChild(tea)

hot_drinks.addChild(coffe)
print(root )