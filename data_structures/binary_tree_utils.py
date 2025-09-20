"""
Problem: Binary Search Tree with Traversals and Utilities
---------------------------------------------------------
We implement a BST that supports:
1. Insertion of elements
2. Searching for an element
3. In-order, pre-order, and post-order traversals
4. Finding minimum and maximum values
5. Calculating the sum of all elements
"""

class BinaryTreeNode:
    def __init__(self, data):
        """Initialize a BST node with data and no children."""
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        """
        Insert a new node into the BST:
        1. Ignore duplicates and None values.
        2. Insert into left if smaller, right if larger.
        """
        if data is None or data == self.data:
            return
        
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinaryTreeNode(data)
        else:  # data > self.data
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinaryTreeNode(data)

    def search(self, data):
        """
        Search for a value in the BST:
        1. Return True if found.
        2. Recursively search left or right subtree based on comparison.
        """
        if self.data == data:
            return True
        elif data < self.data:
            return self.left.search(data) if self.left else False
        else:
            return self.right.search(data) if self.right else False

    def in_order_traversal(self):
        """Return elements in sorted order (left → root → right)."""
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()
        elements.append(self.data)
        if self.right:
            elements += self.right.in_order_traversal()
        return elements

    def pre_order_traversal(self):
        """Return elements in pre-order (root → left → right)."""
        elements = [self.data]
        if self.left:
            elements += self.left.pre_order_traversal()
        if self.right:
            elements += self.right.pre_order_traversal()
        return elements

    def post_order_traversal(self):
        """Return elements in post-order (left → right → root)."""
        elements = []
        if self.left:
            elements += self.left.post_order_traversal()
        if self.right:
            elements += self.right.post_order_traversal()
        elements.append(self.data)
        return elements

    def find_min(self):
        """Return the minimum value in the BST (leftmost node)."""
        current = self
        while current.left:
            current = current.left
        return current.data

    def find_max(self):
        """Return the maximum value in the BST (rightmost node)."""
        current = self
        while current.right:
            current = current.right
        return current.data

    def calculate_sum(self):
        """Return the sum of all elements in the BST."""
        return sum(self.in_order_traversal())


# ------------------ Helper Function ------------------
def build_tree(elements):
    """
    Build a BST from a list of numbers.
    Ignore None values in the list.
    """
    elements = [x for x in elements if x is not None]
    if not elements:
        return None

    root = BinaryTreeNode(elements[0])
    for element in elements[1:]:
        root.add_child(element)
    return root


# ------------------ TESTING ------------------
if __name__ == '__main__':
    nums = [8, 3, 10, 1, 6, None, 14, None, None, 4, 7, 13]
    tree = build_tree(nums)

    print("In-order traversal:", tree.in_order_traversal())   # Sorted order
    print("Minimum value:", tree.find_min())
    print("Maximum value:", tree.find_max())
    print("Sum of all nodes:", tree.calculate_sum())
    print("Pre-order traversal:", tree.pre_order_traversal())
    print("Post-order traversal:", tree.post_order_traversal())
