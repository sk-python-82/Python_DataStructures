class TreeNode:
    def __init__(self,data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self,child):
        child.parent = self
        self.children.append(child)    

    def print_tree(self):
        print(self.data)
        for child in self.children:
            print(child.data)
                                
def buildFamilyTree():
    root  = TreeNode("adam")

    habil = TreeNode("habil")
    root.add_child(habil)
    habil.add_child(TreeNode("ham"))
    habil.add_child(TreeNode("sum"))

    ghabil = TreeNode("ghabil")
    root.add_child(ghabil)
    ghabil.add_child(TreeNode("jum"))
    ghabil.add_child(TreeNode("ghum"))
    return root

root = buildFamilyTree()
root.print_tree()
pass 
