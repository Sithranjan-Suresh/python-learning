"""
Problem: Hospital Queue Management
----------------------------------
Simulates a queue for hospital patients using FIFO (First-In-First-Out) principle.
Operations supported:
1. Enqueue (add a patient)
2. Dequeue (remove the first patient)
3. Peek (view the first patient without removing)
"""

from collections import deque

class HospitalQueue:
    def __init__(self):
        # Initialize an empty deque to store patients
        self.patients = deque()
    
    def enqueue(self, name):
        """
        Add a patient to the end of the queue
        """
        self.patients.append(name)
        print(f"Queue after adding {name}: {list(self.patients)}")

    def dequeue(self):
        """
        Remove and return the first patient from the queue
        """
        if not self.patients:
            return "No patients"
        return self.patients.popleft()
        
    def peek(self):
        """
        View the first patient in the queue without removing
        """
        if not self.patients:
            return "No patients"
        return self.patients[0]

# ------------------ DEMO ------------------
q = HospitalQueue()

# Add patients
q.enqueue("Alice")
q.enqueue("Bob")
q.enqueue("Charlie")

# Check first patient
print("First patient:", q.peek())      # Expected: Alice

# Remove patients
print("Dequeued:", q.dequeue())        # Expected: Alice
print("Dequeued:", q.dequeue())        # Expected: Bob
print("Dequeued:", q.dequeue())        # Expected: Charlie
print("Dequeued:", q.dequeue())        # Expected: No patients
