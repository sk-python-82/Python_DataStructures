"""  print tree"""
class TreeNode:
    """ class"""
    def __init__(self,data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self,child):
        """ add_child"""
        child.parent = self
        self.children.append(child)    

    def print_tree(self):
        """ print_tree"""
        print(self.data)
        if len(self.children) > 0:
            for child in self.children:
                print(child.data)
                print(child.get_level())

    def get_level(self):
        """ get_level """
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level


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
