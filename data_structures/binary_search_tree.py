"""
Problem: Binary Search Tree (BST) Implementation
------------------------------------------------
We implement a BST with the following features:
1. Insert elements while maintaining BST property.
2. Search for an element efficiently.
3. In-order traversal to get elements in sorted order.

Approach:
- Each node has `data`, `left`, and `right`.
- `add_child`: Recursively add a value in the correct subtree.
- `in_order_traversal`: Recursively visit left, root, right.
- `search`: Recursively check left or right based on value comparison.
"""

class BinarySearchTreeNode:
    def __init__(self, data):
        """Initialize a BST node with data and no children."""
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        """
        Add a new node with `data` into the BST.
        1. Ignore duplicates.
        2. If data < node, insert into left subtree.
        3. If data > node, insert into right subtree.
        """
        if data == self.data:
            # Duplicate value, do nothing
            return
        elif data < self.data:
            # Insert into left subtree
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            # Insert into right subtree
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def in_order_traversal(self):
        """
        Return a list of elements in sorted order.
        1. Traverse left subtree
        2. Visit root
        3. Traverse right subtree
        """
        elements = []

        # Visit left subtree
        if self.left:
            elements += self.left.in_order_traversal()

        # Visit root
        elements.append(self.data)

        # Visit right subtree
        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def search(self, val):
        """
        Search for `val` in BST.
        1. If current node matches, return True
        2. If val < current, search left
        3. If val > current, search right
        4. Return False if not found
        """
        if self.data == val:
            return True
        elif val < self.data:
            return self.left.search(val) if self.left else False
        else:
            return self.right.search(val) if self.right else False


def build_tree(elements):
    """
    Build a BST from a list of elements.
    1. First element becomes root.
    2. Insert remaining elements using add_child.
    """
    if not elements:
        return None

    root = BinarySearchTreeNode(elements[0])
    for element in elements[1:]:
        root.add_child(element)
    return root


# ------------------ TESTING ------------------
if __name__ == '__main__':
    numbers = [17, 4, 1, 20, 9, 23, 18, 34]
    numbers_tree = build_tree(numbers)

    # Search test
    print("Search 1 in BST:", numbers_tree.search(1))  # Expected: True
    print("Search 15 in BST:", numbers_tree.search(15))  # Expected: False

    # In-order traversal test
    print("BST in-order traversal (sorted elements):", numbers_tree.in_order_traversal())
