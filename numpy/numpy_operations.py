# Problem: Demonstrate basic properties of NumPy arrays and how to inspect and modify their data types.
# We will create a 2D array, check its properties like dimensions, size, datatype, and memory usage,
# and finally convert the array to a different data type to see how it affects memory usage.

import numpy as np  # Importing NumPy library for numerical operations

# Step 1: Create a 2D NumPy array with 3 rows and 2 columns
a = np.array([[1, 2], [3, 4], [5, 6]])

# Step 2: Print the array to visualize its structure
print("Array:\n", a)

# Step 3: Print the number of dimensions of the array (ndim)
print("Number of dimensions:", a.ndim)

# Step 4: Print the size in bytes of each element in the array (itemsize)
print("Size of each element in bytes:", a.itemsize)

# Step 5: Print the data type of the array elements
print("Data type of array elements:", a.dtype)

# Step 6: Print the total number of elements in the array
print("Total number of elements:", a.size)

# Step 7: Convert the data type of array elements to float64
# This increases the memory used per element since floats are larger than integers
a = a.astype(np.float64)  # Correct way to change dtype in NumPy
print("New data type of array elements:", a.dtype)

# Step 8: Print the new size in bytes of each element after type conversion
print("Size of each element in bytes after conversion:", a.itemsize)
