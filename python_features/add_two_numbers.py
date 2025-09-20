"""
Problem: Add Two Numbers (LeetCode #2)
--------------------------------------
We are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each node contains a single digit. 
We need to add the two numbers and return the sum as a linked list.

Approach:
1. Traverse both linked lists simultaneously.
2. Add corresponding digits along with any carry from the previous step.
3. Create new nodes for each digit in the resulting sum.
4. Continue until both lists and the carry are exhausted.
"""

# Definition for singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val        # The digit value stored in the node
        self.next = next      # Pointer to the next node

class Solution:
    def addTwoNumbers(self, l1, l2):
        # Initialize a dummy head to build the result list
        dummy = ListNode(0)
        current = dummy
        carry = 0  # carry holds any overflow during addition

        # Traverse while there is at least one node in l1, l2, or carry
        while l1 or l2 or carry:
            # Extract values from current nodes (or 0 if none)
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Sum the values plus carry
            total = val1 + val2 + carry
            carry = total // 10   # Carry for the next iteration
            digit = total % 10    # Current digit

            # Append the digit as a new node to the result list
            current.next = ListNode(digit)
            current = current.next

            # Move to the next nodes if available
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        # Return the next of dummy (since dummy is just a placeholder)
        return dummy.next


# ------------------ TESTING ------------------

# Helper function to create a linked list from a Python list
def create_linked_list(values):
    dummy = ListNode(0)
    current = dummy
    for v in values:
        current.next = ListNode(v)
        current = current.next
    return dummy.next

# Helper function to print a linked list as a Python list
def print_linked_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


# Example: [2,4,3] + [5,6,4] = [7,0,8]
list1 = create_linked_list([2, 4, 3])  # Represents number 342
list2 = create_linked_list([5, 6, 4])  # Represents number 465

sol = Solution()
result = sol.addTwoNumbers(list1, list2)
print(print_linked_list(result))  # Output: [7, 0, 8]
