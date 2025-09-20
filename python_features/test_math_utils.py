"""
Problem: Using a custom math utility module
-------------------------------------------
Demonstrates importing a user-defined module and calling a function from it.
"""

# Import custom module math_utils as alias 'pls'
import math_utils as pls

# Call the add function from the module
result = pls.add(1, 2)

# Print the result
print(result)  # Expected output: 3
