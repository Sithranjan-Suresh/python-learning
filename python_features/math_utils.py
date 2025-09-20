"""
Problem: Basic Arithmetic Operations
------------------------------------
Defines functions to perform addition and subtraction of two numbers.
"""

# Function to add two numbers
def add(a, b):
    return a + b

# Function to subtract b from a
def subtract(a, b):
    return a - b

# Example numbers
num1 = 27
num2 = 32

# Demo: print results
print(f"{num1} + {num2} = {add(num1, num2)}")
print(f"{num1} - {num2} = {subtract(num1, num2)}")
