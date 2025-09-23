import numpy as np

# Create a 3x4 numpy array with values from 0 to 11
# np.arange(12) generates numbers from 0 to 11
# .reshape(3, 4) arranges them into a 3-row, 4-column array
a = np.arange(12).reshape(3, 4)
print("Original 3x4 array:\n", a)

print("\nIterating over each element in row-major order (flattened):")
# a.flatten() returns a 1D array in row-major order
for cell in a.flatten():
    print(cell, end=' ')
print() 

print("\nIterating over each element in column-major (Fortran-style) order:")
# np.nditer with order='F' iterates column by column
for x in np.nditer(a, order='F'):
    print(x, end=' ')
print() 

# --- Explanation ---
# 1. We created a 3x4 numpy array with sequential numbers.
# 2. We demonstrated two ways to iterate over all elements:
#    - Using flatten() for row-wise iteration.
#    - Using np.nditer with order='F' for column-wise iteration.
# 3. Printing with end=' ' keeps output on one line for readability.