"""
Problem: Square Numbers Using Generators
----------------------------------------
We create a generator that yields square numbers indefinitely.
1. The generator `square()` yields squares of integers starting from 1.
2. Stop the sequence when a certain condition is met (here, numbers > 25).
"""

# Generator function for square numbers
def square():
    a = 1  # Start from 1
    while True:
        yield a**2  # Yield the square of the current number
        a += 1      # Move to the next number

# ------------------ DEMO ------------------
# Print square numbers up to 25
for i in square():
    if i > 25:
        break
    print(i)
