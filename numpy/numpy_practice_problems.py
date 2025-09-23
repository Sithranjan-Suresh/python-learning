import numpy as np  

# ---------------------------------------------------
# Problem 1: Create a 1D NumPy array of numbers from 10 to 50 (inclusive), 
# then reverse it.
# ---------------------------------------------------

# Create array with numbers from 10 to 50
arr_one = np.arange(10, 51)  
print("Original array (10 to 50):", arr_one)

# Reverse the array using slicing
arr_one_reversed = arr_one[::-1]  
print("Reversed array:", arr_one_reversed)


# ---------------------------------------------------
# Problem 2: Create a 5x5 array filled with random integers between 1 and 100.
# Then print its shape, size, data type, min, max, and mean.
# ---------------------------------------------------

arr_two = np.random.randint(1, 100, size=(5, 5))  
print("\n5x5 Random Array:\n", arr_two)

# Array properties
print("Shape:", arr_two.shape)  
print("Size:", arr_two.size)    
print("Data type:", arr_two.dtype)  

# Array statistics
print("Minimum value:", arr_two.min())  
print("Maximum value:", arr_two.max())  
print("Mean value:", arr_two.mean())  


# ---------------------------------------------------
# Problem 3: Given an array of 20 random integers between 1 and 50, 
# select only the even numbers.
# ---------------------------------------------------

arr_three = np.random.randint(1, 50, size=20)  
print("\nRandom Array of 20 numbers:", arr_three)

# Boolean mask for even numbers
even_mask = (arr_three % 2 == 0)  
print("Even mask:", even_mask)  

# Select only even numbers
print("Even numbers:", arr_three[even_mask])  


# ---------------------------------------------------
# Problem 4: Create a 4×4 random integer matrix (0–9).
# Add 5 to all elements in the second row only (without loops).
# ---------------------------------------------------

arr_four = np.random.randint(0, 10, size=(4, 4))  
print("\nOriginal 4x4 Array:\n", arr_four)

# Add 5 to the entire second row (index 1)
arr_four[1] += 5  
print("Modified 4x4 Array (second row +5):\n", arr_four)
