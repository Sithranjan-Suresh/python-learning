"""
Problem: Fibonacci Sequence Using Generators
---------------------------------------------
We generate Fibonacci numbers indefinitely using a generator.
1. `fib()` is a generator that yields Fibonacci numbers one by one.
2. Stop the sequence when a certain condition is met (here, numbers > 50).
"""

# Generator function for Fibonacci sequence
def fib():
    a, b = 0, 1  # Initialize first two Fibonacci numbers
    while True:
        yield a   # Yield the current number
        a, b = b, a + b  # Move to the next Fibonacci numbers

# ------------------ DEMO ------------------
# Print Fibonacci numbers up to 50
for f in fib():
    if f > 50:
        break
    print(f)
