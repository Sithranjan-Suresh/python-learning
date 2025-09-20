"""
Problem: Read and display contents of a text file
-------------------------------------------------
Reads the entire content of 'input.txt' and prints it to the console.
"""

import json  # Not used in this snippet, only needed if you parse JSON

# Open the file in read mode
with open("input.txt", "r") as f:
    content = f.read()  # Read the full content of the file

# Print file content
print(content)
