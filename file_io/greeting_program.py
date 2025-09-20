"""
Problem: Simple Greeting Program
--------------------------------
Takes user input for name and age, and prints a greeting message.
"""

# Ask user for their name
name = input("What is your name? ")

# Ask user for their age
age = int(input("What is your age? "))

# Print a greeting message with name in uppercase
print(f"Hello {name.upper()}, who is {age} years old")
