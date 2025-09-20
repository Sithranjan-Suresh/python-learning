"""
Problem: Timing Function Execution Using Decorators
---------------------------------------------------
We create a decorator `time_it` that:
1. Wraps any function.
2. Measures the execution time in milliseconds.
3. Prints the time taken.
"""

import time

def time_it(func):
    """
    Decorator to measure execution time of a function in milliseconds.
    """
    def wrapper(*args, **kwargs):
        start = time.time()  # Start time
        result = func(*args, **kwargs)
        end = time.time()    # End time
        elapsed_ms = (end - start) * 1000
        print(f"The operation took {elapsed_ms:.2f} milliseconds")
        return result
    return wrapper


@time_it
def calc_square(numbers):
    """
    Calculate the square of each number in the list.
    Uses list comprehension for efficiency.
    """
    # Using list comprehension instead of appending in loop
    return [i * i for i in numbers]


# ------------------ TESTING ------------------
if __name__ == '__main__':
    # Large array for timing test
    array = [i for i in range(1, 10000000)]
    calc_square(array)
