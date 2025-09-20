"""
Problem: User-Defined Exception Example
---------------------------------------
We define a custom exception class `Accident` that:
1. Inherits from Python's built-in Exception class.
2. Stores a custom error message.
3. Provides a method to print the message.
"""

# Custom Exception Class
class Accident(Exception):
    def __init__(self, msg):
        """
        Initialize the exception with a custom message.
        """
        self.msg = msg

    def print_exception(self):
        """
        Print the custom exception message.
        """
        print("User-defined exception:", self.msg)


# ------------------ DEMO ------------------
try:
    # Raise the custom exception
    raise Accident("Crash between two cars")
except Accident as e:
    # Catch the exception and print the message
    e.print_exception()
