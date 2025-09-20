"""
Problem: Simple Geometry and Pattern Printing Functions
--------------------------------------------------------
We implement:
1. `get_area` function: calculates the area of a rectangle or triangle.
2. `print_pattern` function: prints a right-angled triangle pattern of stars.
"""

print("Hello!")  # Greeting message

# 1️⃣ Function to calculate area
def get_area(length, width, shape):
    """
    Calculate the area of a given shape.
    
    Parameters:
    - length: length of the shape
    - width: width of the shape
    - shape: string, either 'rectangle' or anything else (triangle)
    
    Returns:
    - Area as a number
    """
    shape = shape.lower()
    if shape == "rectangle":
        return length * width
    else:  # Any other shape treated as triangle
        return 0.5 * length * width

# Example usage:
# print(get_area(20, 10, "rectangle"))
# print(get_area(20, 10, "triangle"))

# 2️⃣ Function to print a right-angled triangle pattern
def print_pattern(number):
    """
    Print a right-angled triangle pattern with '*' characters.
    
    Example for number=5:
    *
    **
    ***
    ****
    *****
    """
    for i in range(1, number + 1):
        print('*' * i)  # Print i stars in the ith row

# Example usage
print_pattern(5)
