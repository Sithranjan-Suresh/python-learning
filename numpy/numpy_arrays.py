import numpy as np  # Import the numpy library for array operations

# Create a tuple of lists, each list represents a row of numbers
arr = ([6, 7, 8], [1, 2, 3], [9, 3, 2])

# Access and print the second element of the third row
print("Second element of third row:", arr[2][1])  # Output: 3

# Access and print the last row using negative indexing
print("Last row:", arr[-1])  # Output: [9, 3, 2]

# Create a numpy array for more advanced slicing
a = np.array([6, 7, 8])

# Slice and print elements from index 1 to 2 (inclusive of 1, exclusive of 3)
print("Elements from index 1 to 2 in numpy array 'a':", a[1:3])  # Output: [7 8]

# --- Explanation ---
# We demonstrated how to:
# 1. Create and access elements in a tuple of lists.
# 2. Use indexing to retrieve specific elements and rows.
# 3. Use numpy arrays for efficient slicing and numerical operations.