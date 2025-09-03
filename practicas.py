class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
    def preOrderTraversal(self):
        print(self.data, end=", ")
        if self.left is not None:
            self.left.preOrderTraversal()
        if self.right is not None:
            self.right.preOrderTraversal()
        

root = TreeNode('R')
nodeA = TreeNode('A')
nodeB = TreeNode('B')
nodeC = TreeNode('C')
nodeD = TreeNode('D')
nodeE = TreeNode('E')
nodeF = TreeNode('F')
nodeG = TreeNode('G')

root.left = nodeA
root.right = nodeB

nodeA.left = nodeC
nodeA.right = nodeD

nodeB.left = nodeE
nodeB.right = nodeF

nodeF.left = nodeG


print("hola commit")


root.preOrderTraversal()

#test
print("root.right.left.data:", root.right.left.data)  # Output: E

