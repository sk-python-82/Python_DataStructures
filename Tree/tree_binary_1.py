class Node():
    def __init__(self,value):
        self.left = None
        self.data = value
        self.right = None
class Tree():
    def create_node(self,data):
        return Node(data)
    def insert(self,node,data):
        if node is None:
            return self.create_node(data)
        if data < node.data:
            node.left = self.insert(node.left,data)
        else:
            node.right = self.insert(node.right,data)
        return node
    def traverse_inorder(self,root):
        if root is not None :
            self.traverse_inorder(root.left)
            print(root.data)
            self.traverse_inorder(root.right)
#Driver code
tree = Tree()
root = tree.create_node(5)
print(root.data)
tree.insert(root,2)
tree.insert(root,10)
tree.insert(root,12)
tree.insert(root,23)
tree.insert(root,6)
tree.insert(root,7)
tree.insert(root,8)
tree.insert(root,37)
print("inorder----->")
tree.traverse_inorder(root)
