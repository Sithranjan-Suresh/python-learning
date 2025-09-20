"""
Problem: Hierarchical Product Tree
----------------------------------
Simulates a product hierarchy using a tree structure.
Each node has a name, a parent, and a list of children.
Supports:
1. Adding child nodes
2. Calculating the level of a node
3. Printing the tree with indentation based on level
"""

class TreeNode:
    def __init__(self, data):
        self.data = data          # Name of the node
        self.parent = None        # Reference to parent node
        self.children = []        # List of child nodes
    
    def add_child(self, child):
        """Add a child node and set its parent"""
        child.parent = self
        self.children.append(child)
    
    def get_level(self):
        """Calculate the level of this node in the tree"""
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level
    
    def print_tree(self):
        """Print the tree structure with indentation"""
        spaces = '  ' * self.get_level()
        print(f"{spaces}- {self.data}")
        for child in self.children:
            child.print_tree()


def build_product_tree():
    """Builds a sample product tree and prints it"""
    root = TreeNode("Electronics")

    # Laptop subtree
    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("Surface"))
    laptop.add_child(TreeNode("Thinkpad"))

    # Cell phone subtree
    cellphone = TreeNode("Cell Phone")
    cellphone.add_child(TreeNode("iPhone"))
    cellphone.add_child(TreeNode("Google Pixel"))
    cellphone.add_child(TreeNode("Vivo"))

    # TV subtree
    tv = TreeNode("TV")
    tv.add_child(TreeNode("Samsung"))
    tv.add_child(TreeNode("LG"))

    # Add subtrees to root
    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)

    # Print the entire tree
    root.print_tree()


if __name__ == '__main__':
    build_product_tree()
