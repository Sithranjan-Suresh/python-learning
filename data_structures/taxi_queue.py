"""
Problem: Taxi Queue with VIP Priority
-------------------------------------
Simulates a taxi line where VIP customers get priority.
Operations supported:
1. Arrive (enqueue) with optional VIP status
2. Peek at the first customer
3. Board (dequeue) the first customer
"""

from collections import deque

class TaxiQueue:
    def __init__(self):
        # Initialize an empty deque for the taxi line
        self.taxiline = deque()
    
    def arrive(self, name, vipstatus):
        """
        Add a customer to the queue.
        VIP customers go to the front; normal customers go to the back.
        """
        if vipstatus:
            self.taxiline.appendleft(name)  # VIP → front
        else:
            self.taxiline.append(name)      # Normal → back

    def peek(self):
        """
        View the first customer in line without removing them.
        """
        if not self.taxiline:
            return "No customers"
        return self.taxiline[0]

    def board(self):
        """
        Remove and return the first customer from the queue.
        """
        if not self.taxiline:
            return "No customers"
        return self.taxiline.popleft()


# ------------------ DEMO ------------------
q = TaxiQueue()

# Customers arriving
q.arrive("Alice", False)           # Normal → back
q.arrive("Bob", True)              # VIP → front
q.arrive("Charlie", False)         # Normal → back
q.arrive("David", True)            # VIP → front

# Current queue state
print("Queue state:", list(q.taxiline))

# Peek at first customer
print("First in line:", q.peek())    # Expected: "David"

# Customers boarding
print("Boarded:", q.board())         # Expected: "David"
print("Boarded:", q.board())         # Expected: "Bob"
print("Boarded:", q.board())         # Expected: "Alice"
print("Boarded:", q.board())         # Expected: "Charlie"
print("Boarded:", q.board())         # Expected: "No customers"
