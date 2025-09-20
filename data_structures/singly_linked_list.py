"""
Problem: Singly Linked List Implementation
------------------------------------------
This program implements a basic singly linked list with:
1. Adding a node at the start
2. Adding a node at the end
3. Inserting a node at a specific index
4. Printing the list
"""

# Node class represents each element in the linked list
class Node:
    def __init__(self, data):
        self.data = data  # Store the data
        self.next = None  # Pointer to next node, initially None

# LinkedList class manages the list
class LinkedList:
    def __init__(self):
        self.head = None  # Initially the list is empty

    def print(self):
        """
        Traverse the list and print all nodes
        """
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def add_node_start(self, data):
        """
        Add a new node at the beginning of the list
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def add_node_end(self, data):
        """
        Add a new node at the end of the list
        """
        new_node = Node(data)
        if not self.head:  # If list is empty
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insert_at(self, index, data):
        """
        Insert a new node at a specified index
        """
        if index < 0:
            raise IndexError("Negative index not allowed.")

        if index == 0:
            return self.add_node_start(data)

        new_node = Node(data)
        prev = self.head
        i = 0

        # Traverse to the node just before the desired position
        while prev and i < index-1:
            prev = prev.next
            i += 1

        if prev is None:
            raise IndexError("Index out of bounds.")

        new_node.next = prev.next
        prev.next = new_node

# ------------------ DEMO ------------------
ll = LinkedList()
ll.add_node_start(20)     # List: 20
ll.add_node_start(100)    # List: 100 -> 20
ll.add_node_end(120)      # List: 100 -> 20 -> 120
ll.add_node_end(240)      # List: 100 -> 20 -> 120 -> 240
ll.insert_at(2, 23)       # List: 100 -> 20 -> 23 -> 120 -> 240

ll.print()  # Expected output: 100 -> 20 -> 23 -> 120 -> 240 -> None
