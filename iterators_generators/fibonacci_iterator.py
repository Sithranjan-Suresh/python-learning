"""
Problem: Fibonacci Iterator
---------------------------
Create an iterator class that generates the Fibonacci sequence indefinitely.
"""

class Fibonacci:
    def __init__(self):
        # Initialize first two Fibonacci numbers
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        # Store current value to return
        current = self.a
        # Update to next Fibonacci numbers
        self.a, self.b = self.b, self.a + self.b
        return current

# ------------------ DEMO ------------------
f = Fibonacci()
itr = iter(f)

# Print first 5 Fibonacci numbers
print(next(itr))  # 0
print(next(itr))  # 1
print(next(itr))  # 1
print(next(itr))  # 2
print(next(itr))  # 3
